from libqtile.config import Match
from libqtile.layout import base, columns, floating

from utils import options

layouts: list[base.Layout] = [
    columns.Columns(
        border_focus=options["colour_scheme"]["accent"],
        border_normal=options["colour_scheme"]["border"],
        border_width=1,
        margin=5,
    ),
]

floating_layout: floating.Floating = floating.Floating(
    border_width=0,
    float_rules=[
        *floating.Floating.default_float_rules,
        Match(
            wm_class=[
                "gnome-screenshot",
                "lxappearance",
                "kvantummanager",
                "pavucontrol",
                "MultiMC",
            ]  # type: ignore
        ),
        Match(
            title=[
                "pinentry",
                "Discord Updater",
                "Friends List",
            ]  # type: ignore
        ),
    ]
)
