%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           nekoawai-wallpapers
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai default background
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        make-wallpaper.py
Source1:        metadata.json
Source2:        nekoawai.xml
Source3:        30_nekoawai-wallpaper.gschema.override
Source100:      LICENSE

# The picture is drawn, not shipped: see make-wallpaper.py.
BuildRequires:  python3-base

%description
The background a NekoAwai desktop comes up with: a near-black room lit from
below the bottom edge, drawn from the same palette as the rest of the system.

nekowall replaces it at the first login on a machine that kept nekowall. This
is what a machine that did not keep it looks like, and what the login screen
stands in front of.

openSUSE keeps its own background in the wallpaper-branding slot, and this
package deliberately does not take it: desktop-data-openSUSE asks for
`wallpaper-branding = 84.87.20240405`, an exact version this package cannot
promise and would have to chase. Taking it would make the whole Plasma
profile unresolvable today and would break on any openSUSE bump tomorrow.
The picture is named directly by everything of ours that shows it, which
needs no slot at all.

%prep
cp -p %{SOURCE100} .

%build

%install
install -d %{buildroot}%{_datadir}/wallpapers/NekoAwai/contents/images
python3 %{SOURCE0} \
	%{buildroot}%{_datadir}/wallpapers/NekoAwai/contents/images/2560x1440.png
# Plasma reads the resolution out of the file name and picks the nearest;
# everything else wants a name that does not change.
ln -s 2560x1440.png \
	%{buildroot}%{_datadir}/wallpapers/NekoAwai/contents/images/default.png
install -Dpm 0644 %{SOURCE1} \
	%{buildroot}%{_datadir}/wallpapers/NekoAwai/metadata.json

install -Dpm 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/gnome-background-properties/nekoawai.xml
install -Dpm 0644 %{SOURCE3} \
	%{buildroot}%{_datadir}/glib-2.0/schemas/30_nekoawai-wallpaper.gschema.override

%files
%license LICENSE
%dir %{_datadir}/wallpapers
%dir %{_datadir}/wallpapers/NekoAwai
%dir %{_datadir}/wallpapers/NekoAwai/contents
%dir %{_datadir}/wallpapers/NekoAwai/contents/images
%{_datadir}/wallpapers/NekoAwai/contents/images/2560x1440.png
%{_datadir}/wallpapers/NekoAwai/contents/images/default.png
%{_datadir}/wallpapers/NekoAwai/metadata.json
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/nekoawai.xml
%{_datadir}/glib-2.0/schemas/30_nekoawai-wallpaper.gschema.override

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- The default background, drawn from the palette rather than shipped as art.
