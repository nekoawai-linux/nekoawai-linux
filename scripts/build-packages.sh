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

	missing=
	for source in $sources; do
		[ -f "$dir$source" ] || missing=$source
	done
	if [ -n "$missing" ]; then
		echo "skipped $name: $missing is missing (see ${dir}README.md)"
		continue
	fi

	for source in $sources; do
		cp "$dir$source" "$topdir/SOURCES/"
	done

	rpmbuild -ba "$spec" \
		--define "_topdir $topdir" \
		--define "nekoawai_version $NEKO_VERSION" \
		--define "dist $NEKO_DISTTAG" \
		--define "vendor $NEKO_VENDOR" \
		--define "distribution $NEKO_NAME $NEKO_VERSION" \
		--target "$NEKO_ARCH"
done
