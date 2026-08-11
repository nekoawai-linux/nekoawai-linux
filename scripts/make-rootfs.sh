#!/bin/bash
# Unpack the base into out/rootfs, so its contents can be inspected without
# touching hardware. The steps come from the installer itself: a copy of them
# here would drift.

set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
. "$root/nekoawai.conf"
installer=${NEKO_INSTALLER_SOURCE:-$root/../nekoawai-installer/nekoawai-install}

[ "$(id -u)" -eq 0 ] || { echo "root privileges are required: sudo $0" >&2; exit 1; }
[ -f "$root/out/repo/repodata/repomd.xml" ] || { echo "run make repo first" >&2; exit 1; }
[ -r "$installer" ] || { echo "installer not found: $installer" >&2; exit 1; }

rootfs=$root/out/rootfs
rm -rf "$rootfs"
mkdir -p "$rootfs"

export NEKO_LOCAL_REPO=$root/out/repo
export NEKO_CORE_REPO=$NEKO_UPSTREAM_OSS
. "$installer"
TARGET=$rootfs

install_base
keep_own_packages
apply_service_policy

echo "rootfs: $rootfs"
