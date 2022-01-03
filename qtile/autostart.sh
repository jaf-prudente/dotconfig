#!/bin/sh

# teclado en español
setxkbmap es

# fondo de pantalla
feh --bg-fill /home/jaf/.config/qtile/wallpaper4.png

# transparencias
picom &

# MEGAsync
megasync &

# El polkit para abrir discos duros
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &