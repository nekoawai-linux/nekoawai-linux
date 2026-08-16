%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           nekoawai-filesystem
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        Directories owned by the NekoAwai base
License:        GPL-3.0-or-later
Group:          System/Fhs
URL:            https://nekoawai.moe
BuildArch:      noarch
Source100:      LICENSE

# The FHS skeleton comes from filesystem; only directories written to by
# nekoawai-* components live here.
Requires:       filesystem

%description
Directories owned by the NekoAwai base, so that they do not end up
unowned in the rpm database.

%prep
cp -p %{SOURCE100} .

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/nekoawai
mkdir -p %{buildroot}%{_sharedstatedir}/nekoawai/repo

%files
%license LICENSE
%dir %{_sysconfdir}/nekoawai
%dir %{_sharedstatedir}/nekoawai
# The installer drops the distribution packages here. The directory always
# exists, or the repository from nekoawai-repos would point at nothing.
%dir %{_sharedstatedir}/nekoawai/repo

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- The directories the NekoAwai base writes to, owned rather than left stray.
