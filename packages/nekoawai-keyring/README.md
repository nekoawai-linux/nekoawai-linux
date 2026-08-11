# nekoawai-keyring

This package is built only when the exported public repository signing key
is present in this directory:

    packages/nekoawai-keyring/nekoawai.asc

No key exists for 0.0.1: there is no in-house build yet, and core and extra
point upstream and are verified with the upstream key.
`scripts/build-packages.sh` skips the package while the file is missing.

Once there is a key:

    gpg --armor --export <keyid> > packages/nekoawai-keyring/nekoawai.asc

and `nekoawai-core.repo` gains a `gpgkey=` pointing at
`/usr/lib/rpm/gnupg/keys/nekoawai.asc`.
