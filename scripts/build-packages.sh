#!/bin/bash
# Build the nekoawai-* packages into out/rpmbuild/RPMS.
#
# A package directory is laid out as in OBS: the spec next to its sources,
# no tarball.

set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
. "$root/nekoawai.conf"

topdir=$root/out/rpmbuild
rm -rf "$topdir/BUILD" "$topdir/BUILDROOT" "$topdir/RPMS" \
	"$topdir/SOURCES" "$topdir/SPECS" "$topdir/SRPMS"
mkdir -p "$topdir"/{SOURCES,SPECS,BUILD,RPMS,SRPMS}

# Order does not matter: nothing here build-depends on anything else here.
for dir in "$root"/packages/*/; do
	name=$(basename "$dir")
	spec=$dir$name.spec
	[ -f "$spec" ] || continue

	sources=$(awk -F: '/^Source[0-9]*:/ { gsub(/^[ \t]+/, "", $2); print $2 }' "$spec")

	# A source sits next to its spec, except LICENSE: there is one copy of it
	# at the top of the repository and every package ships that same copy, so
	# that a package taken on its own carries the terms it is under.
	missing=
	for source in $sources; do
		if [ -f "$dir$source" ]; then
			cp "$dir$source" "$topdir/SOURCES/"
		elif [ -f "$root/$source" ]; then
			cp "$root/$source" "$topdir/SOURCES/"
		else
			missing=$source
		fi
	done
	if [ -n "$missing" ]; then
		echo "skipped $name: $missing is missing (see ${dir}README.md)"
		continue
	fi

	rpmbuild -ba "$spec" \
		--define "_topdir $topdir" \
		--define "nekoawai_version $NEKO_VERSION" \
		--define "dist $NEKO_DISTTAG" \
		--define "vendor $NEKO_VENDOR" \
		--define "distribution $NEKO_NAME $NEKO_VERSION" \
		--target "$NEKO_ARCH"
done

# Signing is the difference between a package that says where it came from
# and one that only claims to. Until NEKO_SIGN_KEY names a key the packages
# go out unsigned, and everything downstream -- nekoawai.repo, the installer's
# local repository, rpm-check-signatures in the image -- has to be told to
# accept that. Setting the key is what closes all four at once.
if [ -n "${NEKO_SIGN_KEY:-}" ]; then
	command -v rpmsign >/dev/null || {
		echo "NEKO_SIGN_KEY is set but rpmsign is missing: zypper in rpm-sign" >&2
		exit 1
	}
	mapfile -t -d '' built < <(find "$topdir/RPMS" "$topdir/SRPMS" -name '*.rpm' -print0)
	[ "${#built[@]}" -gt 0 ] || { echo "nothing was built, nothing to sign" >&2; exit 1; }
	rpmsign --addsign --define "_gpg_name $NEKO_SIGN_KEY" "${built[@]}"
	echo "signed ${#built[@]} packages with $NEKO_SIGN_KEY"
else
	echo "NEKO_SIGN_KEY is empty: packages are unsigned, see packages/nekoawai-keyring/README.md"
fi
