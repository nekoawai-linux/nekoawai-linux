Name:           nekowall
Version:        0.5.0
Release:        0%{?dist}
Summary:        Random art from nekos.moe as the NekoAwai wallpaper
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://nekoawai.moe
BuildArch:      x86_64

Source0:        nekowall-0.5.0.tar.gz

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
has none. The window says what happens after that: nothing, a picture at
every login, or a new one every few hours through a timer of its own.

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
#
# Only the login unit. What it does is a setting the program reads, so it can
# be told to do nothing without a symlink changing hands. The rotation timer
# is the user's own decision and is enabled from the window.
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
%{_userunitdir}/nekowall-rotate.service
%{_userunitdir}/nekowall-rotate.timer

%changelog
