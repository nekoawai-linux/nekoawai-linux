%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           patterns-nekoawai-xfce
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai Xfce desktop
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch
Source100:      LICENSE

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

# What the session looks like. Xfce keeps its appearance in branding slots
# that are asked for by the exact version of the package they belong to, so
# this takes none of them: the theme reaches each account from /etc/skel and
# the terminal colours from /etc/xdg, and neither can go stale on an update.
Requires:       nekoawai-branding-xfce

Requires:       polkit-gnome
Requires:       lightdm
Requires:       lightdm-gtk-greeter
Requires:       lightdm-gtk-greeter-branding-upstream
# The look of that screen, as a drop-in beside the file above rather
# than in place of it: the branding slot is asked for by the greeter's
# own version, and no package of ours can promise that number for long.
Requires:       nekoawai-branding-lightdm
Requires:       xdg-desktop-portal-gtk

# Applications the desktop is missing without, and the four panel plugins
# that answer a question the panel raises by existing: what is playing, what
# was copied, what is running, and where is everything else. Weak
# dependencies rather than hard ones: one that leaves the distribution must
# not take the desktop with it.
#
# The xfce4-goodies group entire used to be here, and it is the one place in
# the distribution where a list was copied rather than chosen: a weather
# plugin, a mail watcher, an MPD client and a pair of eyes that follow the
# cursor, on a system whose first rule is that colour marks the one thing
# asking to be pressed. Anyone who wants them types five words at zypper.
Recommends:     mousepad
Recommends:     parole
Recommends:     ristretto
Recommends:     thunar-archive-plugin
Recommends:     xfce4-screensaver
Recommends:     xfce4-screenshooter
Recommends:     xfce4-taskmanager
Recommends:     xfce4-pulseaudio-plugin
Recommends:     xfce4-whiskermenu-plugin
Recommends:     xfce4-clipman-plugin
Recommends:     NetworkManager-applet
# Pairing a device: Xfce has no Bluetooth settings of its own.
Recommends:     blueman

%description
An Xfce session with LightDM, on Xorg. The session packages are listed
directly to avoid pulling the upstream openSUSE base and X11 patterns. The
session itself is the Arch xfce4 group; what sits on top of it was chosen
here rather than taken whole from xfce4-goodies.

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
- The Xfce profile.
- The xfce4-goodies group is no longer taken whole: the panel plugins are chosen.
