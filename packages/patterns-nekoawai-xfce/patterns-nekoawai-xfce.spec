%{!?nekoawai_version:%global nekoawai_version 0.0.1}

Name:           patterns-nekoawai-xfce
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai Xfce desktop
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch

Provides:       pattern() = nekoawai_xfce
Provides:       pattern-visible()
Provides:       pattern-category() = Graphical%%20Environments
Provides:       pattern-order() = 1150

Requires:       patterns-nekoawai-desktop-base
# Xfce is the one X11 session here, and LightDM's greeter is X11 too.
Requires:       patterns-nekoawai-x11

# The Arch xfce4 group, package for package. exo and garcon are libraries on
# openSUSE and arrive with the session; exo-tools is not -- and without it
# "Open Terminal Here" and every other exo-open action fails.
Requires:       exo-tools
Requires:       thunar
Requires:       thunar-volman
Requires:       tumbler
Requires:       xfce4-appfinder
Requires:       xfce4-panel
Requires:       xfce4-power-manager
Requires:       xfce4-session
Requires:       xfce4-session-branding-upstream
Requires:       xfce4-settings
Requires:       xfce4-terminal
Requires:       xfconf
Requires:       xfdesktop
Requires:       xfwm4

# The rest of what archinstall installs with the Xfce profile. openSUSE has
# no xarchiver, so the archive manager Thunar's plugin talks to is
# file-roller.
Requires:       pavucontrol
Requires:       file-roller
Requires:       xfce4-notifyd

Requires:       polkit-gnome
Requires:       lightdm
Requires:       lightdm-gtk-greeter
Requires:       lightdm-gtk-greeter-branding-upstream
Requires:       xdg-desktop-portal-gtk

# The xfce4-goodies group. Weak dependencies rather than hard ones: a plugin
# that leaves the distribution must not take the desktop with it.
Recommends:     mousepad
Recommends:     parole
Recommends:     ristretto
Recommends:     xfburn
Recommends:     thunar-archive-plugin
Recommends:     thunar-media-tags-plugin
Recommends:     xfce4-screensaver
Recommends:     xfce4-screenshooter
Recommends:     xfce4-taskmanager
Recommends:     xfce4-pulseaudio-plugin
Recommends:     xfce4-whiskermenu-plugin
Recommends:     xfce4-clipman-plugin
Recommends:     xfce4-dict
Recommends:     xfce4-notes-plugin
Recommends:     xfce4-battery-plugin
Recommends:     xfce4-cpufreq-plugin
Recommends:     xfce4-cpugraph-plugin
Recommends:     xfce4-diskperf-plugin
Recommends:     xfce4-eyes-plugin
Recommends:     xfce4-fsguard-plugin
Recommends:     xfce4-genmon-plugin
Recommends:     xfce4-mailwatch-plugin
Recommends:     xfce4-mount-plugin
Recommends:     xfce4-mpc-plugin
Recommends:     xfce4-netload-plugin
Recommends:     xfce4-places-plugin
Recommends:     xfce4-sensors-plugin
Recommends:     xfce4-smartbookmark-plugin
Recommends:     xfce4-systemload-plugin
Recommends:     xfce4-time-out-plugin
Recommends:     xfce4-timer-plugin
Recommends:     xfce4-verve-plugin
Recommends:     xfce4-wavelan-plugin
Recommends:     xfce4-weather-plugin
Recommends:     xfce4-xkb-plugin
Recommends:     NetworkManager-applet

%description
An Xfce session with LightDM, on Xorg. The session packages are listed
directly to avoid pulling the upstream openSUSE base and X11 patterns; the
list follows the Arch xfce4 and xfce4-goodies groups, which is what
archinstall installs for the same profile.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
