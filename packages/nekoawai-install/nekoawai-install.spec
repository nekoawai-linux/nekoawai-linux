Name:           nekoawai-install
Version:        0.4.0
Release:        0%{?dist}
Summary:        NekoAwai system installer
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        nekoawai-installer-0.4.0.tar.gz

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
