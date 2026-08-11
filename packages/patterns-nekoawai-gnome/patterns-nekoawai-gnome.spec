%{!?nekoawai_version:%global nekoawai_version 0.0.1}

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
Requires:       gdm
Requires:       gdm-branding-upstream
Requires:       xdg-desktop-portal-gnome
Requires:       xdg-desktop-portal-gtk

Recommends:     gnome-console
Recommends:     nautilus
Recommends:     gnome-control-center
Recommends:     gnome-system-monitor
Recommends:     gnome-text-editor

%description
A lean GNOME session with GDM. Applications beyond the core session are weak
dependencies so the installer can offer minimal and full desktop variants.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
