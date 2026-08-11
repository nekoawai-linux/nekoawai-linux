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
Requires:       thunar
Requires:       thunar-volman
Requires:       xfce4-appfinder
Requires:       xfce4-notifyd
Requires:       xfce4-panel
Requires:       xfce4-power-manager
Requires:       xfce4-session
Requires:       xfce4-session-branding-upstream
Requires:       xfce4-settings
Requires:       xfconf
Requires:       xfdesktop
Requires:       xfwm4
Requires:       polkit-gnome
Requires:       lightdm
Requires:       lightdm-gtk-greeter
Requires:       lightdm-gtk-greeter-branding-upstream
Requires:       xdg-desktop-portal-gtk

Recommends:     xfce4-terminal
Recommends:     NetworkManager-applet
Recommends:     pavucontrol
Recommends:     mousepad
Recommends:     ristretto
Recommends:     xfce4-screenshooter
Recommends:     thunar-archive-plugin

%description
A compact Xfce session with LightDM. The session packages are listed directly
to avoid pulling the upstream openSUSE base and X11 patterns.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
