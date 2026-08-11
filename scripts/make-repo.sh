#!/bin/bash
# Build separate repositories for the target system and Live-only packages.

set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)

repo=$root/out/repo
installer_repo=$root/out/installer-repo
rm -rf "$repo" "$installer_repo"
mkdir -p "$repo" "$installer_repo"

while IFS= read -r -d '' rpm_path; do
	name=$(rpm -qp --qf '%{NAME}' "$rpm_path")
	case $name in
	# Compiled packages leave debuginfo and debugsource behind. Nothing
	# installs them and the target repository travels on the installation
	# medium, so they stay out of it.
	*-debuginfo | *-debugsource) continue ;;
	nekoawai-install) cp "$rpm_path" "$installer_repo/" ;;
	*) cp "$rpm_path" "$repo/" ;;
	esac
done < <(find "$root/out/rpmbuild/RPMS" -name '*.rpm' -print0)

createrepo_c --quiet "$repo"
createrepo_c --quiet "$installer_repo"

echo "target repository:    $repo"
echo "installer repository: $installer_repo"
