#!/bin/bash
# Run the installer against a disk image instead of real hardware.
#
# The disk is a loop device over a file: partitioning and mkfs physically
# cannot escape it, even if the installer picks the wrong device.
#
#   test-install.sh [ext4|btrfs] [yes|no]
#                 filesystem --^        ^-- LUKS2

set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
. "$root/nekoawai.conf"
installer=${NEKO_INSTALLER_SOURCE:-$root/../nekoawai-installer/nekoawai-install}

fstype=${1:-ext4}
encrypt=${2:-no}
size=20G
password=kawaii

if [ "$(id -u)" -ne 0 ]; then
	echo "root privileges are required: pkexec $0" >&2
	exit 1
fi
if [ ! -f "$root/out/repo/repodata/repomd.xml" ]; then
	echo "run make first" >&2
	exit 1
fi
[ -x "$installer" ] || { echo "installer not found: $installer" >&2; exit 1; }
if mountpoint -q /mnt; then
	echo "/mnt is in use and the installer needs it" >&2
	exit 1
fi

image=$root/out/test/nekoawai-$fstype
if [ "$encrypt" = yes ]; then
	image=$image-luks
fi
image=$image.img

mkdir -p "$root/out/test"
rm -f "$image"
truncate -s "$size" "$image"

# Hand the image over up front, not at the end: an interrupted run would
# otherwise leave it owned by root and unusable without privileges.
owner=${PKEXEC_UID:-${SUDO_UID:-0}}
if [ "$owner" != 0 ]; then
	chown "$owner" "$root/out/test" "$image"
fi

loop=$(losetup --find --show --partscan "$image")
trap 'losetup -d "$loop" 2>/dev/null || :' EXIT

# The installer is given a device name only, so make sure it leads to our
# file and not to somebody's disk.
backing=$(losetup -n -O BACK-FILE "$loop")
if [ "$backing" != "$image" ]; then
	echo "$loop points at $backing" >&2
	exit 1
fi

echo "image:  $image"
echo "device: $loop"
echo

# Answers in the order the installer asks for them.
installer_answers() {
	printf '%s\n' "$(basename "$loop")" "$fstype" "$encrypt" yes
	if [ "$encrypt" = yes ]; then
		printf '%s\n' "$password" "$password"
	fi
	# Locale, keymap, timezone and hostname: installer defaults.
	printf '%s\n' '' '' '' ''
	printf '%s\n' "$password" "$password"
	printf '%s\n' no
}

# The bootloader writes a boot entry into the machine's NVRAM, and it would
# point at a loop device that stops existing after the test. A private mount
# namespace with an empty tmpfs over efivars leaves the installer nothing but
# file writes on the ESP.
export NEKO_LOCAL_REPO=$root/out/repo
export NEKO_DETECT_GPU=no
# The single quotes are the point: the body runs in the new namespace, and
# "$1" is the installer path passed to it below, not one expanded here.
# shellcheck disable=SC2016
installer_answers | unshare --mount --propagation private -- bash -c '
	mount -t tmpfs tmpfs /sys/firmware/efi/efivars 2>/dev/null || :
	exec "$1" --text' _ "$installer"

losetup -d "$loop"
trap - EXIT

echo
echo "done: $image"
