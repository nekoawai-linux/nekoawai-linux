%{!?nekoawai_version:%global nekoawai_version 0.0.2}

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
# Trash, removable media and network shares in every file manager. Without
# gvfs a deleted file is a deleted file, with no trash to take it back from.
Requires:       gvfs
Recommends:     gvfs-backends

# What archinstall puts on every desktop regardless of the profile. The base
# already carries nano, wget and the ssh client.
Recommends:     vim
Recommends:     htop
Recommends:     smartmontools

# What the desktop looks like before anyone has chosen anything. Both are
# branding in the openSUSE sense -- packages that take a slot the desktop
# asks for by symbol -- and without them a NekoAwai desktop comes up in
# openSUSE's colours, under openSUSE's picture.
Requires:       nekoawai-branding-gtk
Requires:       nekoawai-wallpapers

# A desktop that comes up grey on the first login says nothing about the
# system it belongs to. nekowall sets one picture at that first login and
# then leaves the choice alone.
#
# Recommended rather than required: it is one of the packages the installer
# offers on its NekoAwai screen, and a screen that offers a choice must be
# able to keep to it. A recommendation is installed unless something says
# otherwise, so ticking nothing changes nothing.
Recommends:     nekowall

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
