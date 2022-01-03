# ESPACIOS DE TRABAJO

from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from .keys import mod, keys

# Los íconos están en https://www.nerdfonts.com/cheat-sheet (se necesita una Nerd Font)

__groups = {
    1: Group("", matches=[Match(wm_class=["firefox"])]), # nf-dev-firefox
    2: Group(""), # nf-mdi-console
    3: Group("ℏ", matches=[Match(wm_class=["texstudio-4.1.1-x86_64.AppImage"])]),
    4: Group(""), # nf-mdi-code_braces
    5: Group(""), # nf-fa-folder_open_o
    6: Group(""), # nf-mdi-view_grid
    7: Group("", matches=[Match(wm_class=["spotify"])]), # nf-fa-spotify
    8: Group("❁")
}

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend([
        # ALTERNA ESPACIOS DE TRABAJO
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # MUEVE LA VENTANA SELECCIONADA A OTRO ESPACIO DE TRABAJO
        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])