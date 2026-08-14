%{!?nekoawai_version:%global nekoawai_version 0.0.2}

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
Source3:        console-colours.service
Source4:        vtrgb

Requires:       systemd
Requires:       zram-generator
# setvtrgb. systemd pulls kbd in for the keymap; the palette is the other
# thing in that package NekoAwai has an opinion about.
Requires:       kbd

%description
Defaults for NekoAwai system services. Shipped as drop-ins under /usr so
that the administrator can override them from /etc.

Including the sixteen colours of the text console, which are the same
sixteen the terminal in a session is given: a machine without a desktop is
the machine this distribution is written for, and it should not have to look
like a machine nobody chose.

%build

%install
install -Dpm 0644 %{SOURCE0} \
	%{buildroot}%{_prefix}/lib/systemd/journald.conf.d/50-nekoawai.conf
install -Dpm 0644 %{SOURCE1} \
	%{buildroot}%{_prefix}/lib/systemd/zram-generator.conf
install -Dpm 0644 %{SOURCE2} \
	%{buildroot}%{_prefix}/lib/systemd/system/getty@.service.d/50-nekoawai.conf
install -Dpm 0644 %{SOURCE3} \
	%{buildroot}%{_prefix}/lib/systemd/system/nekoawai-console-colours.service
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_datadir}/nekoawai/vtrgb

%files
%dir %{_prefix}/lib/systemd/journald.conf.d
%{_prefix}/lib/systemd/journald.conf.d/50-nekoawai.conf
%{_prefix}/lib/systemd/zram-generator.conf
%dir %{_prefix}/lib/systemd/system/getty@.service.d
%{_prefix}/lib/systemd/system/getty@.service.d/50-nekoawai.conf
%{_prefix}/lib/systemd/system/nekoawai-console-colours.service
%dir %{_datadir}/nekoawai
%{_datadir}/nekoawai/vtrgb

%changelog
