%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           nekoawai-branding-xfce
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai look for the Xfce session
License:        GPL-3.0-or-later
Group:          System/GUI/XFCE
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        xsettings.xml
Source1:        terminalrc
Source2:        nekoawai.theme
Source100:      LICENSE

Requires:       nekoawai-branding-gtk

%description
What an Xfce session looks like on NekoAwai: the dark Adwaita the rest of the
system is set to, and a terminal in the sixteen colours the text console
already uses.

Xfce keeps its appearance in nine branding slots, and two of them -- the
theme and the backdrop -- are the ones worth having. Neither is taken. Both
are required by exact version (xfce4-settings-branding = 4.20.5), so a
package holding one would stop satisfying it the next time Xfce moved, and
`zypper dup` would answer that by replacing this package with openSUSE's:
the desktop would quietly return to somebody else's colours on an ordinary
update. That is the shape of the worst defect this distribution has had, and
it is not worth a settings file.

So the theme arrives as the account's own copy, out of /etc/skel, where
nothing can take it away and the user can. The backdrop stays with nekowall,
which sets one at the first login and is the answer to that question
everywhere else as well.

%prep
cp -p %{SOURCE100} .

%build

%install
install -Dpm 0644 %{SOURCE0} \
	%{buildroot}%{_sysconfdir}/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
install -Dpm 0644 %{SOURCE1} \
	%{buildroot}%{_sysconfdir}/xdg/xfce4/terminal/terminalrc
install -Dpm 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/xfce4/terminal/colorschemes/nekoawai.theme

%files
%license LICENSE
%dir %{_sysconfdir}/skel/.config
%dir %{_sysconfdir}/skel/.config/xfce4
%dir %{_sysconfdir}/skel/.config/xfce4/xfconf
%dir %{_sysconfdir}/skel/.config/xfce4/xfconf/xfce-perchannel-xml
%{_sysconfdir}/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/terminal
%config(noreplace) %{_sysconfdir}/xdg/xfce4/terminal/terminalrc
%dir %{_datadir}/xfce4
%dir %{_datadir}/xfce4/terminal
%dir %{_datadir}/xfce4/terminal/colorschemes
%{_datadir}/xfce4/terminal/colorschemes/nekoawai.theme

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- The Xfce theme and terminal palette, laid down in /etc/skel.
