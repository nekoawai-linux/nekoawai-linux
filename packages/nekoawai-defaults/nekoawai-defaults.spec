%{!?nekoawai_version:%global nekoawai_version 0.0.1}

Name:           nekoawai-defaults
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai system service defaults
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        journald.conf
Source1:        zram-generator.conf
Source2:        getty.conf

Requires:       systemd
Requires:       zram-generator

%description
Defaults for NekoAwai system services. Shipped as drop-ins under /usr so
that the administrator can override them from /etc.

%build

%install
install -Dpm 0644 %{SOURCE0} \
	%{buildroot}%{_prefix}/lib/systemd/journald.conf.d/50-nekoawai.conf
install -Dpm 0644 %{SOURCE1} \
	%{buildroot}%{_prefix}/lib/systemd/zram-generator.conf
install -Dpm 0644 %{SOURCE2} \
	%{buildroot}%{_prefix}/lib/systemd/system/getty@.service.d/50-nekoawai.conf

%files
%dir %{_prefix}/lib/systemd/journald.conf.d
%{_prefix}/lib/systemd/journald.conf.d/50-nekoawai.conf
%{_prefix}/lib/systemd/zram-generator.conf
%dir %{_prefix}/lib/systemd/system/getty@.service.d
%{_prefix}/lib/systemd/system/getty@.service.d/50-nekoawai.conf

%changelog
