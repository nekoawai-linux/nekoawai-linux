%{!?nekoawai_version:%global nekoawai_version 0.0.2}

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
# SDDM greets on Wayland here, so the profile needs no X server.
Requires:       sddm-qt6

# What archinstall installs with the Hyprland profile: a bare compositor has
# no notifications, terminal, launcher, file manager or screenshot tool, and
# no way to ask for a password.
Requires:       dunst
Requires:       kitty
Requires:       uwsm
Requires:       wofi
Requires:       dolphin
Requires:       polkit-kde-agent-6
Requires:       grim
Requires:       slurp
# Qt applications default to the X11 backend when the Wayland plugin is
# missing, which then needs Xwayland for anything Qt.
Requires:       libqt5-qtwayland
Requires:       qt6-wayland

Recommends:     waybar
Recommends:     hyprpaper
Recommends:     hyprpicker
Recommends:     NetworkManager-applet

%description
A Hyprland session with SDDM and native screen-cast and screenshot portals.
The tool selection follows the archinstall Hyprland profile.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
