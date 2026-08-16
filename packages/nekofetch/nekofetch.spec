Name:           nekofetch
Version:        0.1.0
Release:        0%{?dist}
Summary:        Compact Linux system information for NekoAwai
License:        GPL-3.0-or-later
Group:          System/Console
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        nekofetch-0.1.0.tar.gz

BuildRequires:  make
Requires:       bash
Recommends:     iproute2

%description
nekofetch prints a compact summary of the operating system, host, kernel,
architecture, network address and uptime.

%prep
%setup -q

%build

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/nekofetch

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.1.0-0
- nekofetch 0.1.0.
