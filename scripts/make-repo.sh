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
	if [ "$name" = nekoawai-install ]; then
		cp "$rpm_path" "$installer_repo/"
	else
		cp "$rpm_path" "$repo/"
	fi
done < <(find "$root/out/rpmbuild/RPMS" -name '*.rpm' -print0)

createrepo_c --quiet "$repo"
createrepo_c --quiet "$installer_repo"

echo "target repository:    $repo"
echo "installer repository: $installer_repo"
