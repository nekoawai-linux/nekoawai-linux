%{!?nekoawai_version:%global nekoawai_version 0.0.2}

Name:           patterns-nekoawai-gnome
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai GNOME desktop
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch

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
Recommends:     gnome-software
Recommends:     gnome-tour
Recommends:     simple-scan
Recommends:     snapshot
Recommends:     yelp

%description
A GNOME session with GDM. The session comes from the upstream gnome_basis
pattern; the applications follow the Arch gnome group, which is what
archinstall installs for the same profile.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
