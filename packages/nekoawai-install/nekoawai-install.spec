Name:           nekoawai-install
Version:        0.5.0
Release:        0%{?dist}
Summary:        NekoAwai system installer
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        nekoawai-installer-0.5.0.tar.gz

BuildRequires:  make
Requires:       /bin/bash
Requires:       coreutils
Requires:       cryptsetup
Requires:       dosfstools
Requires:       dracut
Requires:       e2fsprogs
Requires:       btrfsprogs
Requires:       NetworkManager-tui
Requires:       openssl
Requires:       parted
Requires:       rpm
Requires:       shadow
Requires:       systemd
Requires:       systemd-boot
Requires:       util-linux
Requires:       zypper

%description
The NekoAwai Live installer provides an interactive configuration menu for
partitioning, profiles, users, networking and systemd-boot.

%prep
%setup -q -n nekoawai-installer-%{version}

%build

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/nekoawai-install

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.5.0-0
- nekoawai-install 0.5.0.
- The chosen keymap is loaded on the console before any password is typed,
  and written into the installed system for graphical sessions too.
- The disk list offers only what can hold a system: no more boot medium, no
  more zram, ram disks or the empty floppy drive a hypervisor invents.
- The disk is checked for room before it is erased, not eight minutes after.
- A failed install says what is on the disk instead of "nothing was written".
- Signatures are checked against the keys on the medium, not against keys
  imported from the network they are meant to vouch for.
- btrfs roots are mounted and recorded with compress=zstd:1.
