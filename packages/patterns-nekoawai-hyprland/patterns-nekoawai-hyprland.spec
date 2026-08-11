%{!?nekoawai_version:%global nekoawai_version 0.0.1}

Name:           patterns-nekoawai-hyprland
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai Hyprland desktop
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch

Provides:       pattern() = nekoawai_hyprland
Provides:       pattern-visible()
Provides:       pattern-category() = Graphical%%20Environments
Provides:       pattern-order() = 1120

Requires:       patterns-nekoawai-desktop-base
Requires:       hyprland
Requires:       xdg-desktop-portal-hyprland
Requires:       xdg-desktop-portal-gtk
Requires:       polkit-gnome
Requires:       sddm-qt6

Recommends:     kitty
Recommends:     rofi-wayland
Recommends:     mako
Recommends:     waybar
Recommends:     grim
Recommends:     slurp
Recommends:     hyprpaper
Recommends:     hyprpicker
Recommends:     thunar
Recommends:     NetworkManager-applet

%description
A Hyprland session with SDDM and native screen-cast and screenshot portals.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
