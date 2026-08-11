# nekofetch

This package is built only when the release archive of the utility is
present in this directory:

    packages/nekofetch/nekofetch-0.1.0.tar.gz

The archive is a build artifact of the sibling project and is not kept in
this repository. Produce it from there:

    make -C ../nekofetch dist
    cp ../nekofetch/dist/nekofetch-0.1.0.tar.gz .

`scripts/build-packages.sh` skips the package while the file is missing, so
the rest of the repositories still build. The version in `Source0` and the
version of the archive have to match.
