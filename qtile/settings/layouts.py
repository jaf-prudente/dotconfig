# CAPAS DE FORMATO DE VENTANAS

from libqtile import layout
from libqtile.config import Match
from .theme import colors

moradito = "#a000dc"

layout_conf = {
    'border_normal': "#222222",
    'border_focus': colors['focus'][0],
    'border_width': 2,
    'single_border_width': 0,
    'margin': 1,
    'single_margin': 0
}

layouts = [
    layout.Columns(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    # layout.RatioTile(**layout_conf),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=moradito
)
