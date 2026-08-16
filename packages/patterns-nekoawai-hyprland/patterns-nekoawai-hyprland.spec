%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           patterns-nekoawai-hyprland
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai Hyprland desktop
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch
Source100:      LICENSE

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
# grim writes a file and stops there. Without wl-clipboard a screenshot
# cannot reach the application it was taken for, and a terminal cannot copy
# a line out to anything else: on Wayland the clipboard is a program, not a
# part of the compositor.
Requires:       wl-clipboard
# A session that cannot be locked is a session that cannot be walked away
# from. Niri got swaylock the day it was written; this profile did not, and
# the omission has been sitting in the one desktop most likely to be used on
# a laptop.
Requires:       hyprlock
Requires:       hypridle
# Qt applications default to the X11 backend when the Wayland plugin is
# missing, which then needs Xwayland for anything Qt.
Requires:       libqt5-qtwayland
Requires:       qt6-wayland

Recommends:     waybar
Recommends:     hyprpaper
Recommends:     hyprpicker
Recommends:     NetworkManager-applet
# Pairing a device without a settings application of its own.
Recommends:     blueman

%description
A Hyprland session with SDDM and native screen-cast and screenshot portals.
The tool selection follows the archinstall Hyprland profile.

%prep
cp -p %{SOURCE100} .

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%license LICENSE
%dir %{_docdir}/%{name}

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- The Hyprland profile.
- hyprlock and hypridle added: the session could not be locked.
- wl-clipboard added: grim could only write a screenshot to a file.
