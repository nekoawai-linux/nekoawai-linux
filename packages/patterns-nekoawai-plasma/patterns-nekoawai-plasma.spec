%{!?nekoawai_version:%global nekoawai_version 0.0.1}

Name:           patterns-nekoawai-plasma
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai KDE Plasma desktop
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch

Provides:       pattern() = nekoawai_plasma
Provides:       pattern-visible()
Provides:       pattern-category() = Graphical%%20Environments
Provides:       pattern-order() = 1140

Requires:       patterns-nekoawai-desktop-base
Requires:       patterns-kde-kde_plasma
Requires:       sddm-qt6
Requires:       xdg-desktop-portal-kde6

Recommends:     konsole
Recommends:     dolphin
Recommends:     ark
Recommends:     kate
Recommends:     spectacle
Recommends:     plasma6-systemmonitor

%description
A lean KDE Plasma Wayland session with SDDM and the KDE portal backend.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
