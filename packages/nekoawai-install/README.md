# nekoawai-install

This package is built only when the release archive of the installer is
present in this directory:

    packages/nekoawai-install/nekoawai-installer-0.2.0.tar.gz

The archive is a build artifact of the sibling project and is not kept in
this repository. Produce it from there:

    make -C ../nekoawai-installer dist
    cp ../nekoawai-installer/dist/nekoawai-installer-0.2.0.tar.gz .

`scripts/build-packages.sh` skips the package while the file is missing, so
the rest of the repositories still build. The version in `Source0` and the
version of the archive have to match.
