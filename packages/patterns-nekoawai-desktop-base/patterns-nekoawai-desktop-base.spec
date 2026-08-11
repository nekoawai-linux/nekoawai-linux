%{!?nekoawai_version:%global nekoawai_version 0.0.1}

Name:           patterns-nekoawai-desktop-base
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai common desktop system
License:        GPL-3.0-or-later
Group:          Metapackages
URL:            https://nekoawai.moe
BuildArch:      noarch

Provides:       pattern() = nekoawai_desktop_base
Provides:       pattern-category() = Graphical%%20Environments
Provides:       pattern-order() = 1100

Requires:       patterns-nekoawai-base

# Graphics and Wayland/X11 compatibility.
Requires:       Mesa
Requires:       libvulkan1
Requires:       xwayland

# Audio and desktop integration.
Requires:       pipewire
Requires:       pipewire-alsa
Requires:       pipewire-pulseaudio
Requires:       wireplumber
Requires:       polkit
Requires:       NetworkManager
Requires:       xdg-desktop-portal
Requires:       xdg-user-dirs
Requires:       xdg-utils
Requires:       desktop-file-utils
Requires:       shared-mime-info

# Every session needs a usable fallback font set.
Requires:       fontconfig
Requires:       dejavu-fonts
Requires:       google-noto-sans-fonts

%description
Graphics, audio, desktop integration and fonts shared by every NekoAwai
desktop profile. Compositors, display managers and portal backends belong to
the selected profile.

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

%files
%dir %{_docdir}/%{name}

%changelog
