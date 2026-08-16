%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           patterns-nekoawai-x11
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai Xorg display server
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch
Source100:      LICENSE

Provides:       pattern() = nekoawai_x11
Provides:       pattern-category() = Graphical%%20Environments
Provides:       pattern-order() = 1090

# Nothing in a session drags the X server in on its own: lightdm requires
# only `xdm`, a configuration package, and the Xfce parts ask for libX11 and
# get it from Mesa's dependencies. A profile that runs on Xorg -- or brings a
# greeter that does -- has to name the server, and this is where it is named.
# archinstall installs xorg-server and xorg-xinit for the same reason;
# openSUSE keeps the input driver and the core fonts outside the server
# package, so both are listed here as well.
Requires:       xorg-x11-server
Requires:       xinit
Requires:       xauth
Requires:       xf86-input-libinput
Requires:       xorg-x11-fonts-core

Recommends:     xorg-x11-driver-video
Recommends:     xorg-x11-essentials
Recommends:     xorg-x11-fonts
Recommends:     xorg-x11-server-extra

%description
The Xorg display server, its input driver and the fonts it needs to start.
Required by profiles whose session or login greeter runs on X11 rather than
Wayland.

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
- The Xorg server, for the profiles whose greeter needs one.
