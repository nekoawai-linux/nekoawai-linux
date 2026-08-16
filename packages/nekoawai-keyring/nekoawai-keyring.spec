%{!?nekoawai_version:%global nekoawai_version 0.0.3}

Name:           nekoawai-keyring
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai repository signing keys
License:        GPL-3.0-or-later
Group:          System/Packages
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        nekoawai.asc
Source100:      LICENSE

Requires(post): rpm

%description
Public keys the NekoAwai repositories are signed with.

%prep
cp -p %{SOURCE100} .

%build

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_prefix}/lib/rpm/gnupg/keys/nekoawai.asc

%post
# The key must reach the rpm database before the first signature check.
rpmkeys --import %{_prefix}/lib/rpm/gnupg/keys/nekoawai.asc || :

%files
%license LICENSE
%{_prefix}/lib/rpm/gnupg/keys/nekoawai.asc

%changelog
* Sun Aug 16 2026 shizukiq <261241967+shizukiq@users.noreply.github.com> - 0.0.3-0
- The public half of the repository signing key. Not built until a key exists.
