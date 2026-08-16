#!/bin/bash
# Build separate repositories for the target system and Live-only packages.

set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
. "$root/nekoawai.conf"

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

# The signature over repomd.xml is what makes the list of packages as
# trustworthy as the packages themselves: without it a repository can be
# rewritten to offer an older signed build, and every signature still checks
# out. The key goes beside it so that a fresh machine can pick it up before
# it has anything of ours installed.
if [ -n "${NEKO_SIGN_KEY:-}" ]; then
	for directory in "$repo" "$installer_repo"; do
		gpg --batch --yes --local-user "$NEKO_SIGN_KEY" \
			--detach-sign --armor "$directory/repodata/repomd.xml"
		gpg --batch --yes --armor --export "$NEKO_SIGN_KEY" \
			> "$directory/repodata/repomd.xml.key"
	done
	echo "metadata signed with $NEKO_SIGN_KEY"
fi

echo "target repository:    $repo"
echo "installer repository: $installer_repo"
