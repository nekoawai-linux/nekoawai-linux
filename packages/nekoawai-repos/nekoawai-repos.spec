%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           nekoawai-repos
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai package repositories
License:        GPL-3.0-or-later
Group:          System/Packages
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        nekoawai-core.repo
Source1:        nekoawai-extra.repo
Source2:        nekoawai.repo
Source100:      LICENSE

Requires:       zypper
# The repository directory has to exist before nekoawai.repo points at it.
Requires:       nekoawai-filesystem

%description
The repositories the system gets its packages from.

In 0.0.3 core and extra point at the openSUSE Tumbleweed binary base, since
there is no in-house build yet. When there is, only baseurl changes: the
repository names and everything referring to them stay as they are.

The third repository, nekoawai, sits on the machine itself and holds the
distribution's own packages. Without it they are orphans in the system, and
the first zypper dup removes them in favour of openSUSE-release.

%prep
cp -p %{SOURCE100} .

%build

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/zypp/repos.d/nekoawai-core.repo
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/zypp/repos.d/nekoawai-extra.repo
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/zypp/repos.d/nekoawai.repo

%files
%license LICENSE
%dir %{_sysconfdir}/zypp
%dir %{_sysconfdir}/zypp/repos.d
%config(noreplace) %{_sysconfdir}/zypp/repos.d/nekoawai-core.repo
%config(noreplace) %{_sysconfdir}/zypp/repos.d/nekoawai-extra.repo
%config(noreplace) %{_sysconfdir}/zypp/repos.d/nekoawai.repo

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- core and extra move to https, and metadata signatures are checked again:
-   repo_gpgcheck=0 accepted an older signed package as readily as today's.
