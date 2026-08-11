%{!?nekoawai_version:%global nekoawai_version 0.0.1}

Name:           patterns-nekoawai-niri
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai Niri desktop
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch

Provides:       pattern() = nekoawai_niri
Provides:       pattern-visible()
Provides:       pattern-category() = Graphical%%20Environments
Provides:       pattern-order() = 1110

Requires:       patterns-nekoawai-desktop-base
Requires:       niri
Requires:       xwayland-satellite
Requires:       xdg-desktop-portal-gnome
Requires:       xdg-desktop-portal-gtk
Requires:       gnome-keyring
Requires:       polkit-gnome
Requires:       lightdm
Requires:       lightdm-gtk-greeter
Requires:       lightdm-gtk-greeter-branding-upstream

Recommends:     alacritty
Recommends:     fuzzel
Recommends:     mako
Recommends:     waybar
Recommends:     swaybg
Recommends:     swayidle
Recommends:     swaylock
Recommends:     NetworkManager-applet

%description
A usable Niri session with LightDM and the portal backends selected by
Niri's upstream portal configuration.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
