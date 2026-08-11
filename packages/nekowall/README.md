# nekowall

This package is built only when the release archive of the utility is
present in this directory:

    packages/nekowall/nekowall-0.2.1.tar.gz

The archive is a build artifact of the sibling project and is not kept in
this repository. Produce it from there:

    make -C ../nekowall dist
    cp ../nekowall/dist/nekowall-0.2.1.tar.gz .

`scripts/build-packages.sh` skips the package while the file is missing, so
the rest of the repositories still build. The version in `Source0` and the
version of the archive have to match.

Unlike the other packages here this one compiles: it needs `cmake`, a C++
compiler and `qt6-base-devel` on the build machine.
