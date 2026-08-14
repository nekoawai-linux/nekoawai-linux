%{!?nekoawai_version:%global nekoawai_version 0.0.2}

Name:           nekoawai-release
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai release identity
License:        GPL-3.0-or-later
Group:          System/Fhs
URL:            https://nekoawai.moe

# The hooks zypper and third-party software identify the distribution by.
Provides:       distribution-release = %{version}-%{release}
Provides:       product() = NekoAwai
Provides:       product(NekoAwai) = %{version}-%{release}
Provides:       product-label() = NekoAwai
Provides:       product-cpeid() = cpe%%3A%%2Fo%%3Anekoawai%%3Anekoawai%%3A%{version}
# A system has exactly one identity: openSUSE-release owns the same paths
# and declares the same distribution-release.
Conflicts:      distribution-release
Conflicts:      openSUSE-release

%description
The files that decide what the system calls itself: os-release, issue and
the product record for libzypp.

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib %{buildroot}%{_sysconfdir}/products.d

# ID_LIKE: the binary base of 0.0.2 comes from openSUSE Tumbleweed and
# third-party scripts should behave accordingly. Goes away together with the
# move to in-house builds.
cat > %{buildroot}%{_prefix}/lib/os-release <<'EOF'
NAME="NekoAwai"
ID=nekoawai
ID_LIKE="opensuse suse"
VERSION="%{version}"
VERSION_ID="%{version}"
PRETTY_NAME="NekoAwai %{version}"
CPE_NAME="cpe:/o:nekoawai:nekoawai:%{version}"
ANSI_COLOR="0;35"
HOME_URL="https://nekoawai.moe"
BUG_REPORT_URL="https://nekoawai.moe/bugs"
EOF

ln -s ..%{_prefix}/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# The installed system gets an identity line only. The welcome and temporary
# credentials belong to the Live image, which has a separate lifecycle.
cat > %{buildroot}%{_sysconfdir}/issue <<'EOF'
NekoAwai %{version} (\l) - \s \r \m
EOF

cat > %{buildroot}%{_sysconfdir}/issue.net <<'EOF'
NekoAwai %{version}
EOF

cat > %{buildroot}%{_sysconfdir}/products.d/nekoawai.prod <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<product schemeversion="0">
  <vendor>NekoAwai</vendor>
  <name>NekoAwai</name>
  <version>%{version}</version>
  <!-- Exactly the package release: otherwise libzypp compares this record
       against product() from the repository, sees a mismatch and offers a
       "product update" on every dup. -->
  <release>%{release}</release>
  <arch>%{_target_cpu}</arch>
  <productline>NekoAwai</productline>
  <cpeid>cpe:/o:nekoawai:nekoawai:%{version}</cpeid>
  <summary>NekoAwai</summary>
  <shortsummary>NekoAwai</shortsummary>
  <description>NekoAwai %{version}</description>
  <linguas>
    <language>en_US</language>
  </linguas>
  <urls>
    <url name="homepage">https://nekoawai.moe</url>
  </urls>
  <installconfig>
    <distribution>NekoAwai</distribution>
    <defaultlang>en_US</defaultlang>
  </installconfig>
  <runtimeconfig/>
</product>
EOF

ln -s nekoawai.prod %{buildroot}%{_sysconfdir}/products.d/baseproduct

%files
%{_prefix}/lib/os-release
%config %{_sysconfdir}/os-release
%config(noreplace) %{_sysconfdir}/issue
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/products.d
%{_sysconfdir}/products.d/nekoawai.prod
%{_sysconfdir}/products.d/baseproduct

%changelog
