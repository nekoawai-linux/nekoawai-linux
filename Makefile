.PHONY: all packages repo rootfs test-install clean

all: repo

packages:
	scripts/build-packages.sh

repo: packages
	scripts/make-repo.sh

# Needs root, so it deliberately does not depend on repo: otherwise sudo
# would build the packages as root and the next plain make could not
# overwrite them. Build the repository with a separate make.
rootfs:
	scripts/make-rootfs.sh

# Also needs root: the installer works on a block device.
test-install:
	scripts/test-install.sh

clean:
	rm -rf out
