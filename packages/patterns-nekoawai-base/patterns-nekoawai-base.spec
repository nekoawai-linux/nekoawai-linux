%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           patterns-nekoawai-base
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai base system
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch
Source100:      LICENSE

Provides:       pattern() = base
Provides:       pattern-visible()
# A value with a space would be parsed as several provides.
Provides:       pattern-category() = Base%%20Technologies
Provides:       pattern-order() = 1010
# There can be only one base pattern, and the upstream one drags in
# openSUSE-release.
Conflicts:      patterns-base-base

# --- boot / kernel
Requires:       kernel-default
# The target hardware is unknown in advance, so take all firmware rather than
# the virtual kernel-firmware, which anyone may satisfy tomorrow.
#
# Recommended rather than required, and it is the one place where that word
# is about size: the set is the largest single thing in the base, and on a
# virtual machine -- the only place 0.0.3 has ever run -- not one file of it
# is ever read. The installer decides: it names the package on real hardware
# and locks it under a hypervisor, so neither case depends on the solver's
# mood. A base put down without the installer keeps the firmware, which is
# the safe way round.
Recommends:     kernel-firmware-all
Requires:       systemd-boot
# All ESP work goes through sdbootutil. It is also the condition by which
# the kernel package scriptlet decides where to put a new kernel: without it
# kernel updates never reach the ESP and the system stays on the old one.
Requires:       sdbootutil
Requires:       efibootmgr
Requires:       dracut
Requires:       kmod
# Microcode carries errata fixes for the CPU itself and is needed before
# anything else on real hardware; dracut folds it into the initramfs on its
# own once the package is there. The target CPU is unknown in advance.
Requires:       ucode-intel
Requires:       ucode-amd

# --- libc runtime
Requires:       glibc
# The full locale set rather than -base: base holds C and en_US only, and
# any other locale chosen during install would be broken.
Requires:       glibc-locale
Requires:       libgcc_s1
Requires:       libstdc++6

# --- GNU userspace
Requires:       bash
Requires:       coreutils
Requires:       util-linux
Requires:       findutils
Requires:       grep
Requires:       sed
Requires:       gawk
Requires:       diffutils
Requires:       tar
Requires:       gzip
Requires:       bzip2
Requires:       xz
Requires:       zstd
Requires:       gettext-runtime
Requires:       patch
Requires:       file
Requires:       which
Requires:       less
Requires:       nano
Recommends:     bash-completion

# --- documentation
# A system without graphics explains itself: manual pages are part of the
# base, not something fetched later.
Recommends:     man
Recommends:     man-pages

# --- hardware diagnostics
# Without graphics, the only way to find out what you are running on.
Recommends:     pciutils
Recommends:     usbutils
Recommends:     dmidecode

# --- system
Requires:       aaa_base
Requires:       systemd
Requires:       dbus-broker
Requires:       shadow
Requires:       pam
Requires:       pam-config
Requires:       acl
Requires:       attr
Requires:       libcap-progs
Requires:       procps
Requires:       terminfo-base
Requires:       timezone
# Swap in compressed memory instead of a partition: takes no disk space,
# works with an encrypted root, and the layout does not depend on it.
Requires:       zram-generator

# --- package stack
Requires:       rpm
Requires:       libzypp
Requires:       zypper
# The keys the base is signed with, in the system rather than fetched at the
# moment they are needed to check something. nekoawai-core.repo checks both
# packages and metadata, and a check has nothing to stand on without these.
# The package also carries the unit that follows openSUSE's key rotations, so
# the trust survives the base moving underneath it.
Requires:       openSUSE-build-key

# --- network
Requires:       NetworkManager
# Networking is configured by hand here, and nmcli is painful enough for
# Wi-Fi that the tui belongs in the base as much as NetworkManager itself.
Requires:       NetworkManager-tui
# The base listens on nothing, but a system installed on someone else's
# machine must not depend on that staying true.
Requires:       firewalld
Requires:       iproute2
Requires:       iputils
Requires:       iw
Requires:       wpa_supplicant
Requires:       curl
Recommends:     wget
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Requires:       openssl
Requires:       openssh-clients
# Shipped but disabled by preset: half the uses of a headless system are
# "install it and log in over ssh", and that is the worst moment to discover
# the server is missing. It listens only after an explicit enable.
Requires:       openssh-server

# --- filesystem / storage
Requires:       e2fsprogs
Requires:       btrfsprogs
# Scrub and balance on timers: unattended btrfs quietly accumulates errors
# and fills up with metadata.
Requires:       btrfsmaintenance
Requires:       dosfstools
Requires:       parted
Requires:       cryptsetup

# --- NekoAwai
Requires:       nekoawai-release
Requires:       nekoawai-filesystem
Requires:       nekoawai-setup
Requires:       nekoawai-repos
Requires:       nekoawai-systemd-presets
Requires:       nekoawai-defaults
# Everything above is the system's own identity and is not up for discussion.
# nekofetch is a program that prints a summary: the installer offers it on
# its NekoAwai screen, and a screen that offers a choice must be able to keep
# to it. The installer installs it by name, so the recommendation only
# matters where the base is put down without one.
Recommends:     nekofetch

%description
The NekoAwai base system: boot, userspace, systemd, the package stack,
networking and storage. The agreed contents of the 0.0.3 base.

%prep
cp -p %{SOURCE100} .

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%license LICENSE
%dir %{_docdir}/%{name}

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- The agreed contents of the 0.0.3 base.
- openSUSE-build-key is required: signature checking needs the key in the system.
- kernel-firmware-all is recommended, and the installer decides by hardware.
