%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           patterns-nekoawai-niri
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai Niri desktop
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch
Source100:      LICENSE

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
# On Wayland the clipboard is a program. Without it nothing copied in a
# terminal reaches anything else on the screen.
Requires:       wl-clipboard

Recommends:     NetworkManager-applet
# Pairing a device without a settings application of its own.
Recommends:     blueman

%description
A usable Niri session with LightDM and the portal backends selected by
Niri's upstream portal configuration. The tool selection follows the
archinstall Niri profile.

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
- The Niri profile.
- wl-clipboard added: on Wayland the clipboard is a program, not the compositor.
