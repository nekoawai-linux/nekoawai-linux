%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           nekoawai-systemd-presets
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai service enablement policy
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        50-nekoawai.preset
Source100:      LICENSE

# systemd requires the symbol, not a particular package, so we take the
# slot instead of systemd-presets-branding-openSUSE.
Provides:       systemd-presets-branding = %{version}
Conflicts:      systemd-presets-branding

%description
Decides which units get enabled when packages are installed.

%prep
cp -p %{SOURCE100} .

%build

%install
install -Dpm 0644 %{SOURCE0} \
	%{buildroot}%{_prefix}/lib/systemd/system-preset/50-nekoawai.preset

%files
%license LICENSE
%{_prefix}/lib/systemd/system-preset/50-nekoawai.preset

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- What the base starts and what it leaves alone.
- bluetooth.service is enabled where bluez is installed at all.
