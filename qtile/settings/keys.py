# ATAJOS DE TECLADO

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [

    #------------ CONFIGURACIÓN DE VENTANAS ------------
    # CONFIGURACIÓN DE VENTANAS (FOCO)
    ([mod], "Left", lazy.layout.left()),
    ([mod], "Right", lazy.layout.right()),
    ([mod], "Down", lazy.layout.down()),
    ([mod], "Up", lazy.layout.up()),

    # CONFIGURACIÓN DE VENTANAS (TAMAÑO)
    ([mod, "control"], "Left", lazy.layout.grow_left()),
    ([mod, "control"], "Right", lazy.layout.grow_right()),
    ([mod, "control"], "Down", lazy.layout.grow_down()),
    ([mod, "control"], "Up", lazy.layout.grow_up()),
    ([mod], "n", lazy.layout.normalize()),

    # CONFIGURACIÓN DE VENTANAS (POSICION)
    ([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    ([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    ([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    ([mod, "shift"], "Up", lazy.layout.shuffle_up()),

    # ALTERNA LAYOUT
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # CERRADO DE VENTANAS
    ([mod], "q", lazy.window.kill()),

    # CAMBIA DE MONITOR SELECCIONADO
    ([mod, "mod1"], "Left", lazy.next_screen()),
    ([mod, "mod1"], "Right", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    #------------ CONFIGURACIÓN DE APLICACIONES ------------

    # Rofi
    ([mod], "space", lazy.spawn("rofi -show drun -show-icons")),
    ([mod, "mod1"], "space", lazy.spawn("rofi -show")),

    # Firefox
    ([mod], "b", lazy.spawn("firefox")),

    # TexStudio
    ([mod], "l", lazy.spawn("./Documentos/TexStudio/texstudio-4.1.1-x86_64.AppImage")),

    # Nautilus
    ([mod], "e", lazy.spawn("nautilus")),

    # VSCode
    ([mod], "v", lazy.spawn("./Documentos/VSCode-linux-x64/bin/code")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -P -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot -s")),

    # spotify
    ([mod], "m", lazy.spawn("snap run spotify &")),

    # ------------ CONFIGURACIÓN DE HARDWARE ------------

    # Volume
    #([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    #([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    #([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness
    #([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    #([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
