%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           nekoawai-branding-gtk
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai defaults for GTK applications
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        settings.ini
Source1:        settings-gtk4.ini
Source2:        30_nekoawai-interface.gschema.override
Source100:      LICENSE

# Adwaita-dark is a separate package from the toolkit; without it GTK falls
# back to a theme from before the century turned, and quietly.
Requires:       gtk3-metatheme-adwaita
Requires:       adwaita-icon-theme

# Two slots, one decision: the same look on both toolkits, or applications
# from the two of them side by side in different colours.
Provides:       gtk3-branding = %{version}
Conflicts:      gtk3-branding
Provides:       gtk4-branding = %{version}
Conflicts:      gtk4-branding

%description
What a GTK application looks like on a NekoAwai desktop before anyone has
chosen anything: the dark variant of Adwaita, with Adwaita icons and cursors
under it.

Note that openSUSE ties its own branding to the exact version of the toolkit
it was built against. This one does not: it holds a decision, not a copy of
the toolkit's defaults, and there is nothing in it to go stale on an update.

%prep
cp -p %{SOURCE100} .

%build

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/gtk-3.0/settings.ini
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/gtk-4.0/settings.ini
install -Dpm 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/glib-2.0/schemas/30_nekoawai-interface.gschema.override

%files
%license LICENSE
%dir %{_sysconfdir}/gtk-3.0
%config(noreplace) %{_sysconfdir}/gtk-3.0/settings.ini
%dir %{_datadir}/gtk-4.0
%{_datadir}/gtk-4.0/settings.ini
%{_datadir}/glib-2.0/schemas/30_nekoawai-interface.gschema.override

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- The dark Adwaita decision, held in the gtk3 and gtk4 branding slots.
