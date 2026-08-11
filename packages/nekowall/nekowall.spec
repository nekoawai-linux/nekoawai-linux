Name:           nekowall
Version:        0.2.0
Release:        0%{?dist}
Summary:        Random art from nekos.moe as the NekoAwai wallpaper
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://nekoawai.moe
BuildArch:      x86_64

Source0:        nekowall-0.2.0.tar.gz

BuildRequires:  cmake >= 3.22
BuildRequires:  gcc-c++
BuildRequires:  qt6-base-devel

# Everything the program itself needs comes from Qt and is picked up as a
# library dependency. What sets the wallpaper belongs to the desktop, and the
# desktop patterns already carry it -- except swaybg, which is the fallback
# for a Wayland session that has nothing of its own.
Recommends:     swaybg

%description
nekowall builds a wallpaper of exactly the screen's resolution out of a
random picture from nekos.moe: a picture close to the screen's shape covers
it, and anything else -- most of the gallery is portrait -- is laid whole on
a blurred copy of itself. The artist is recorded next to the wallpaper.

A systemd user unit sets one wallpaper at the first login of a system that
has none. After that it is a window and a command.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%post
# User units are enabled for everyone at once: there is no user yet when the
# installer runs, and every user of a NekoAwai desktop is meant to get one.
systemctl --global enable nekowall.service >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ]; then
	systemctl --global disable nekowall.service >/dev/null 2>&1 || :
fi

%files
%license LICENSE
%doc README.md
%{_bindir}/nekowall
%{_datadir}/applications/nekowall.desktop
%{_userunitdir}/nekowall.service

%changelog
