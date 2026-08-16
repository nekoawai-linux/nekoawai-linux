%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           nekoawai-setup
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai account and login environment policy
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        nekoawai.sh
Source1:        50-nekoawai
Source100:      LICENSE

# 0.0.3 builds on top of aaa_base rather than replacing it: passwd, group,
# shells and profile still belong upstream. Our own versions arrive when
# aaa_base goes.
Requires:       aaa_base
Requires:       shadow
# The group has to exist in every NekoAwai system rather than appear by
# accident, so that accounts added later can be put into it.
Requires:       system-group-wheel
# sudo is what gives membership in wheel any meaning; see 50-nekoawai.
Requires:       sudo

%description
NekoAwai account and login environment policy.

%prep
cp -p %{SOURCE100} .

%build

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/profile.d/nekoawai.sh
install -Dpm 0440 %{SOURCE1} %{buildroot}%{_sysconfdir}/sudoers.d/50-nekoawai

%files
%license LICENSE
%config %{_sysconfdir}/profile.d/nekoawai.sh
%dir %{_sysconfdir}/sudoers.d
%config(noreplace) %attr(0440,root,root) %{_sysconfdir}/sudoers.d/50-nekoawai

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- sudo through wheel, without targetpw, and /usr/sbin on a regular PATH.
