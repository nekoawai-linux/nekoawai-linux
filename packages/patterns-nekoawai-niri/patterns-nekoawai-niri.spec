%{!?nekoawai_version:%global nekoawai_version 0.0.2}

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
# The session is Wayland, but LightDM's greeter is an X11 program: without a
# server the machine boots into a display manager that cannot draw.
Requires:       patterns-nekoawai-x11
Requires:       niri
Requires:       xwayland-satellite
Requires:       xdg-desktop-portal-gnome
Requires:       xdg-desktop-portal-gtk
Requires:       gnome-keyring
Requires:       polkit-gnome
Requires:       lightdm
Requires:       lightdm-gtk-greeter
Requires:       lightdm-gtk-greeter-branding-upstream
# The look of that screen, as a drop-in beside the file above rather
# than in place of it: the branding slot is asked for by the greeter's
# own version, and no package of ours can promise that number for long.
Requires:       nekoawai-branding-lightdm

# The tools archinstall installs with the Niri profile. A scrolling
# compositor ships no terminal, launcher or lock screen of its own, so these
# are the session, not extras.
Requires:       alacritty
Requires:       fuzzel
Requires:       mako
Requires:       waybar
Requires:       swaybg
Requires:       swayidle
Requires:       swaylock

Recommends:     NetworkManager-applet

%description
A usable Niri session with LightDM and the portal backends selected by
Niri's upstream portal configuration. The tool selection follows the
archinstall Niri profile.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
