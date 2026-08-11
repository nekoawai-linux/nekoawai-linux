%{!?nekoawai_version:%global nekoawai_version 0.0.1}

Name:           nekoawai-filesystem
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        Directories owned by the NekoAwai base
License:        GPL-3.0-or-later
Group:          System/Fhs
URL:            https://nekoawai.moe
BuildArch:      noarch

# The FHS skeleton comes from filesystem; only directories written to by
# nekoawai-* components live here.
Requires:       filesystem

%description
Directories owned by the NekoAwai base, so that they do not end up
unowned in the rpm database.

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/nekoawai
mkdir -p %{buildroot}%{_sharedstatedir}/nekoawai/repo

%files
%dir %{_sysconfdir}/nekoawai
%dir %{_sharedstatedir}/nekoawai
# The installer drops the distribution packages here. The directory always
# exists, or the repository from nekoawai-repos would point at nothing.
%dir %{_sharedstatedir}/nekoawai/repo

%changelog
