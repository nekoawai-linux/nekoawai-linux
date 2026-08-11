%{!?nekoawai_version:%global nekoawai_version 0.0.1}

Name:           nekoawai-keyring
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai repository signing keys
License:        GPL-3.0-or-later
Group:          System/Packages
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        nekoawai.asc

Requires(post): rpm

%description
Public keys the NekoAwai repositories are signed with.

%build

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_prefix}/lib/rpm/gnupg/keys/nekoawai.asc

%post
# The key must reach the rpm database before the first signature check.
rpmkeys --import %{_prefix}/lib/rpm/gnupg/keys/nekoawai.asc || :

%files
%{_prefix}/lib/rpm/gnupg/keys/nekoawai.asc

%changelog
