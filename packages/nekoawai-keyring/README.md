# nekoawai-keyring

This package is built only when the exported public repository signing key
is present in this directory:

    packages/nekoawai-keyring/nekoawai.asc

No key exists for 0.0.3, and `scripts/build-packages.sh` skips the package
while the file is missing. `nekoawai-core` and `nekoawai-extra` point
upstream and are verified with the upstream key, which arrives with
`openSUSE-build-key` as part of the base pattern.

## What the missing key costs

One absent key is four separate holes, and they close together:

| where | what it says today |
| --- | --- |
| `packages/nekoawai-repos/nekoawai.repo` | `gpgcheck=0` |
| `nekoawai-install`, local repository | `--no-gpgcheck` |
| `nekoawai-iso/config.xml` | `<rpm-check-signatures>false</rpm-check-signatures>` |
| this package | not built |

Nothing else is waiting on anything else. The private half is a decision
about custody rather than a build step, which is why it is not in this
repository and no script creates one.

## Making the key

The key belongs to whoever holds the release, on a machine that is not a
build runner:

    gpg --batch --quick-generate-key \
        'NekoAwai Package Signing Key <shizukiq@nekoawai.moe>' \
        ed25519 sign 5y

Export the public half into this directory, and keep the private half and
its revocation certificate off every machine that builds:

    gpg --armor --export 'NekoAwai Package Signing Key' \
        > packages/nekoawai-keyring/nekoawai.asc

## Turning it on

Set the key in `nekoawai.conf`, or in the environment for one build:

    NEKO_SIGN_KEY='NekoAwai Package Signing Key' make

From there everything follows on its own:

- `scripts/build-packages.sh` signs every rpm and srpm it builds;
- `scripts/make-repo.sh` signs `repomd.xml` and writes `repomd.xml.key`
  beside it;
- `nekoawai-iso/scripts/build.sh` sees the signed metadata and builds the
  image with `rpm-check-signatures` on;
- `nekoawai-keyring` is built, because `nekoawai.asc` now exists.

Two files then change by hand, and only once: `nekoawai.repo` goes to
`gpgcheck=1` with `gpgkey=file:///usr/lib/rpm/gnupg/keys/nekoawai.asc`, and
the installer drops `--no-gpgcheck` from the local repository it adds during
the install.
