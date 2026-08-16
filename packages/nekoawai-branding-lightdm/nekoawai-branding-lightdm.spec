%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           nekoawai-branding-lightdm
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai login screen
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        50-nekoawai.conf
Source100:      LICENSE

# The drop-in directory arrived in 2.0.1. Naming the version is also what
# keeps this package out of the branding slot: the greeter asks for
# lightdm-gtk-greeter-branding >= 2.0.8, a number that belongs to the greeter
# and would have to be chased here for ever.
Requires:       lightdm-gtk-greeter >= 2.0.1

# The greeter is a session of its own and reads none of the settings a user
# session has: the theme has to be named to it, and the picture has to exist
# before anybody has logged in to choose one.
Requires:       nekoawai-branding-gtk
Requires:       nekoawai-wallpapers

%description
The screen the Xfce and Niri profiles show before a login: the NekoAwai
background, dark Adwaita over it, and nothing else added to it.

A drop-in beside the greeter's own configuration rather than a replacement
of it, so that an update to the greeter cannot arrive with a conflict.

%prep
cp -p %{SOURCE100} .

%build

%install
install -Dpm 0644 %{SOURCE0} \
	%{buildroot}%{_sysconfdir}/lightdm/lightdm-gtk-greeter.conf.d/50-nekoawai.conf

%files
%license LICENSE
%dir %{_sysconfdir}/lightdm
%dir %{_sysconfdir}/lightdm/lightdm-gtk-greeter.conf.d
%config(noreplace) %{_sysconfdir}/lightdm/lightdm-gtk-greeter.conf.d/50-nekoawai.conf

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- The greeter in the NekoAwai palette, as a drop-in beside the upstream branding.
