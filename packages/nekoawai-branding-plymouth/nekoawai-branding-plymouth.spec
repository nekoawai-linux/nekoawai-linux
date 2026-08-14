%{!?nekoawai_version:%global nekoawai_version 0.0.2}

Name:           nekoawai-branding-plymouth
Version:        %{nekoawai_version}
Release:        0%{?dist}
Summary:        NekoAwai boot screen policy
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://nekoawai.moe
BuildArch:      noarch

Source0:        plymouthd.defaults

# plymouth requires the symbol and openSUSE's provider brings a splash with
# its own mascot on it. Nothing in NekoAwai installs plymouth, so this is not
# required by anything either: it arrives with plymouth, if plymouth ever
# arrives.
Provides:       plymouth-branding = %{version}
Conflicts:      plymouth-branding
Supplements:    plymouth

%description
The boot screen NekoAwai asks for, which is the boot: messages rather than a
picture over them.

Not because a picture would be wrong, but because it would take artwork this
project does not have, images for the passphrase dialog, and a virtual
machine to prove both in. The file says as much, and changing the decision
later is one line.

%build

%install
install -Dpm 0644 %{SOURCE0} \
	%{buildroot}%{_datadir}/plymouth/plymouthd.defaults

%files
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/plymouthd.defaults

%changelog
