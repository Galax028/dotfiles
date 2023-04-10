#!/bin/bash

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst -config $HOME/.config/dunst/dunstrc &
picom --config $HOME/.config/picom/picom.conf --experimental-backend --backend="glx" &
