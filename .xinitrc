#!/bin/sh

# Initialize Nvidia card
xrandr --setprovideroutputsource modesetting NVIDIA-0
xrandr --auto

# Run xinitrc.d files
if [ -d /etc/X11/xinit/xinitrc.d ]; then
    for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
        [ -x "$f" ] && . "$f"
    done
    unset f
fi

# G502 mouse settings
ratbagctl hollering-marmot profile active set 0
# xinput --set-prop "Logitech G502 HERO Gaming Mouse" 185 2 0 0 0 2 0 0 0 1
xinput --set-prop "Logitech G502 HERO Gaming Mouse" 215 2 0 0 0 2 0 0 0 1

# Start Qtile
exec qtile start

