%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           patterns-nekoawai-gnome
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai GNOME desktop
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch
Source100:      LICENSE

Provides:       pattern() = nekoawai_gnome
Provides:       pattern-visible()
Provides:       pattern-category() = Graphical%%20Environments
Provides:       pattern-order() = 1130

Requires:       patterns-nekoawai-desktop-base
Requires:       patterns-gnome-gnome_basis
# GDM greets on Wayland, so the profile needs no X server.
Requires:       gdm
Requires:       gdm-branding-upstream
Requires:       xdg-desktop-portal-gnome
Requires:       xdg-desktop-portal-gtk

# The Arch gnome group, as far as openSUSE ships it. What is left out are the
# sharing and remote-access services -- gnome-remote-desktop, gnome-user-share
# and rygel -- which open ports on a machine that asked for a desktop.
Requires:       nautilus
Requires:       gnome-console
Requires:       gnome-control-center
Requires:       gnome-keyring
Requires:       gnome-menus
Requires:       gnome-system-monitor
Requires:       gnome-text-editor
Requires:       gnome-tweaks
Requires:       xdg-user-dirs-gtk
Requires:       file-roller
Requires:       loupe
Requires:       papers

Recommends:     baobab
Recommends:     epiphany
Recommends:     gnome-calculator
Recommends:     gnome-calendar
Recommends:     gnome-characters
Recommends:     gnome-clocks
Recommends:     gnome-color-manager
Recommends:     gnome-connections
Recommends:     gnome-contacts
Recommends:     gnome-disk-utility
Recommends:     gnome-font-viewer
Recommends:     gnome-logs
Recommends:     gnome-maps
# gnome-software is deliberately absent. It reads AppStream metadata, and
# NekoAwai publishes none: the store comes up empty, and what it does find it
# offers under openSUSE's product name, including distribution upgrades this
# system has no channel for. A software centre that lies about what the
# machine is running is worse than no software centre. zypper is the answer
# until there is metadata of our own to give it.
Recommends:     gnome-tour
Recommends:     simple-scan
Recommends:     snapshot
Recommends:     yelp

%description
A GNOME session with GDM. The session comes from the upstream gnome_basis
pattern; the applications follow the Arch gnome group, which is what
archinstall installs for the same profile.

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
- The GNOME profile.
- gnome-software dropped: NekoAwai publishes no AppStream metadata for it to read.
