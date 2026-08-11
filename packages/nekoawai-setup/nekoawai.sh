# NekoAwai login environment defaults. The base /etc/profile comes from
# aaa_base; this only adds to it.

if [ -z "$EDITOR" ]; then
	EDITOR=nano
	export EDITOR
fi

# System utilities live in /usr/sbin, which is not in a regular user's
# PATH: swapon, lsblk and ip are not found, and "command not found" reads as
# "not installed". This changes visibility, not privileges.
case ":$PATH:" in
*:/usr/sbin:*) ;;
*) PATH="$PATH:/usr/sbin"; export PATH ;;
esac
