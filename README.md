<div align="center">

# NekoAwai

=^..^=

![Release](https://img.shields.io/github/v/release/nekoawai-linux/nekoawai-linux?include_prereleases&label=NekoAwai%20Release&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/nekoawai-linux/nekoawai-linux?style=for-the-badge&color=%23daaa3f)
![License](https://img.shields.io/github/license/nekoawai-linux/nekoawai-linux?color=green&style=for-the-badge)
[![Website](https://img.shields.io/badge/Website-nekoawai.moe-%23e32b6b?style=for-the-badge)](https://nekoawai.moe)

**A small, comfy Linux on the rpm, libzypp and zypper stack, with systemd and systemd-boot.**

Made by one person who wanted a machine that feels like somebody lives in it.

</div>

## Is it safe to use?

Not yet. NekoAwai 0.0.2 partitions, installs and boots to a login prompt, and
that is the whole of what has been verified, in virtual machines. There is no
signing key, no update channel of its own, and no installation on real
hardware behind it. Keep it in a virtual machine.

If you want a distribution to keep your data on, install openSUSE Tumbleweed.
NekoAwai is built from it and gives you nothing it does not.

## What 0.0.2 is

A derivative, not an independent build. The binary base comes from openSUSE
Tumbleweed and is still stamped `Vendor: openSUSE`: kernel, glibc, systemd,
userspace. What NekoAwai owns is its identity packages and its installer.

It becomes a distribution of its own once the base is rebuilt from source
under `Vendor: NekoAwai` with the `.na1` disttag. The repository is laid out
for that: only `NEKO_UPSTREAM_*` in `nekoawai.conf` and the `baseurl`s in
`nekoawai-repos` change.

The swap works because openSUSE keeps its identity in separate packages:
`systemd` requires the symbol `systemd-presets-branding` rather than a
specific package, and `distribution-release` and `product()` come from the
release package. `nekoawai-systemd-presets` and `nekoawai-release` take those
slots.

## The five repositories

The distribution is small enough to read in an evening, and it is kept in
pieces so that each one can be read on its own:

| | |
| --- | --- |
| **nekoawai-linux** | this one: RPM specs, patterns, distribution policy |
| [nekoawai-installer](https://github.com/nekoawai-linux/nekoawai-installer) | the Live installer, from partitions to the bootloader |
| [nekoawai-iso](https://github.com/nekoawai-linux/nekoawai-iso) | the recipe for the bootable Live image |
| [nekowall](https://github.com/nekoawai-linux/nekowall) | the wallpaper picker every desktop profile carries |
| [nekofetch](https://github.com/nekoawai-linux/nekofetch) | the system summary a headless machine is asked for |

The last two are ordinary programs with their own versions and their own
release archives. The installer offers them by name and will happily leave
them out.

## Build

    make                # target and installer repositories into out/
    sudo make rootfs    # unpack the base into out/rootfs to inspect it

`nekoawai-install` and `nekofetch` are packaged from the release archives of
their own projects. Those archives are build artifacts and are not kept here,
so both packages are skipped until you produce them; see
`packages/nekoawai-install/README.md` and `packages/nekofetch/README.md`.

## Layout

    nekoawai.conf       build identity and upstream of the base
    packages/           one directory per package, as in OBS
    scripts/            packages, repository, rootfs, install test

| Package | Owns |
| --- | --- |
| `nekoawai-release` | os-release, console welcome, libzypp product record |
| `nekoawai-filesystem` | directories belonging to the base |
| `nekoawai-setup` | accounts and login environment |
| `nekofetch` | independently released system information command |
| `nekowall` | independently released wallpaper picker, on the desktops |
| `nekoawai-wallpapers` | the background a desktop comes up with |
| `nekoawai-branding-gtk` | the look of GTK applications |
| `nekoawai-branding-xfce` | the look of the Xfce session |
| `nekoawai-branding-lightdm` | the login screen |
| `nekoawai-branding-plymouth` | what the boot screen shows, if there is one |
| `nekoawai-repos` | repositories of the installed system |
| `nekoawai-keyring` | repository signing keys |
| `nekoawai-systemd-presets` | which units get enabled |
| `nekoawai-defaults` | defaults of system services, and the console palette |
| `nekoawai-install` | installer |
| `patterns-nekoawai-base` | the contents of the base |
| `patterns-nekoawai-x11` | the Xorg server, for the profiles that need one |

`out/repo` is the target-system repository; the Live-only installer is routed
to `out/installer-repo`.

The contents of the base are not duplicated anywhere:
`patterns-nekoawai-base.spec` is both what a human reads and what the
installer installs (`zypper install patterns-nekoawai-base`, aka `@base`).

## Installer

`nekoawai-install` is a Live-only installer for UEFI machines: GPT, a 512 MiB
ESP, an ext4 or btrfs root, optional LUKS2, Minimal or one desktop profile,
users, NetworkManager, swap, additional packages, dracut and systemd-boot. It
lives in [nekoawai-installer](https://github.com/nekoawai-linux/nekoawai-installer).

Its package screen also offers the packages NekoAwai writes itself --
`nekowall` on a desktop, `nekofetch` on any system -- ticked by default and
each one refusable. That is why the patterns recommend them rather than
require them: the installer names the ones that were kept and locks the ones
that were not for the length of the transaction, so the answer given on the
screen is the one the finished system has.

The bootloader is driven by `sdbootutil`: the installer writes
`/etc/kernel/cmdline` and lets it lay out the ESP. The kernel package's
scriptlet calls the same tool on every update, so new kernels reach the ESP on
their own.

The installer copies the distribution's own packages into
`/var/lib/nekoawai/repo` and the installed system keeps them as a repository.
Without that they would be orphans, and the first `zypper dup` would drop them
in favour of `openSUSE-release`.

    scripts/test-install.sh [ext4|btrfs] [yes|no]

runs the whole installation against a loop-mounted disk image instead of real
hardware.

## Will there be other desktops?

There are patterns for Niri, Hyprland, GNOME, Plasma and Xfce, and the
installer offers all five. Only Xfce has been installed and started end to
end so far. The rest are composed but unproven, and proving them is the kind
of work that needs more than one person.

What goes into a desktop profile follows archinstall's profile of the same
name, package for package, translated to the openSUSE names. archinstall has
had years of reports about what a session is missing on a machine that was
minimal an hour ago, and there is nothing to gain from making those
discoveries a second time. Where openSUSE ships no equivalent -- `xarchiver`,
for one -- the nearest package that does the job takes its place, and the spec
says so.

`patterns-nekoawai-x11` carries the Xorg server for the profiles that need
one. Nothing else pulls it in: `lightdm` requires only the `xdm`
configuration package, so a profile with an X11 greeter that does not name the
server boots into a display manager that cannot draw.

Applications are chosen for a small system that explains itself: the base is
a working CLI machine with networking, firewall and manual pages before any
desktop is added.

## What it looks like

openSUSE keeps its appearance in packages of its own and asks for them by
symbol -- `gtk3-branding`, `plymouth-branding`, `wallpaper-branding` -- which
is the same door `nekoawai-systemd-presets` and `nekoawai-release` walked
through to make this a distribution at all. A NekoAwai desktop came up in
openSUSE's colours because nothing here had walked through it yet.

Some of those slots can be held and some cannot, and the difference is one
word in the requirement. `plymouth` asks for `plymouth-branding` and names no
version; nothing versions `gtk3-branding` either. But `desktop-data-openSUSE`
asks for `wallpaper-branding = 84.87.20240405`, `xfce4-settings` for
`xfce4-settings-branding = 4.20.5`, and `lightdm-gtk-greeter` for
`lightdm-gtk-greeter-branding >= 2.0.8`. A package of ours sitting in one of
those stops satisfying it the first time the upstream package moves, and
`zypper dup` repairs that the only way it can: openSUSE's branding back,
ours removed. The desktop would return to somebody else's colours on an
ordinary update, quietly. That is defect 16 in different clothes, and it is
not worth a settings file.

So three slots are held -- `gtk3-branding`, `gtk4-branding`,
`plymouth-branding` -- and everything else is done beside them, in places
nothing else is looking:

| | |
| --- | --- |
| the Xfce theme | the account's own copy, laid down in `/etc/skel` |
| the login screen | a drop-in in `lightdm-gtk-greeter.conf.d` |
| the GNOME background | a gsettings override that sorts after openSUSE's |
| the text console | `setvtrgb` from a unit, before `getty.target` |

One palette runs through all of it. The sixteen colours of the text console
are the sixteen of the terminal inside a session, the login screen stands in
front of the same picture the desktop has, and the background is drawn from
the palette rather than shipped as art: `make-wallpaper.py` is the picture,
and the PNG is a build artifact like any other. Red, green and yellow keep
their meanings everywhere, because a log that has gone red has to look it.

None of it has been started in a virtual machine. What has been checked is
that all five profiles and the base still resolve against the live
repositories, and that is a different sentence.

## Contributing

The repository packages a distribution; it does not host application code.
Keep changes inside the project that owns them: RPM specs and distribution
policy here, the installer and `nekofetch` in their own repositories, the Live
image in [nekoawai-iso](https://github.com/nekoawai-linux/nekoawai-iso).

Shell scripts use `set -euo pipefail`, quote their expansions and stay
focused. Comments explain why, not what. Everything user-facing is written in
English.

Work that came from somebody else is named in
[CONTRIBUTORS.md](CONTRIBUTORS.md).

## License

Copyright (c) 2026 shizukiq. GPL-3.0-or-later; see `LICENSE`. Packages taken
from openSUSE Tumbleweed keep their own licenses.

<sub><sub>[donate in TON](https://tonviewer.com/UQAj-bErFKSDkHqy_5RSwkKxmkE3RgATMLFHp-TYX5JN2kHe)</sub></sub>
