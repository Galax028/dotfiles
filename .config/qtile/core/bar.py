from libqtile.bar import Bar

from utils import options
from widgets import (
    Clock,
    GroupBox,
    Keyboard,
    Logo,
    Separator,
    Systray,
    Wifi,
    WindowName,
)

defaults: dict[str, object] = {
    "font": options["fonts"]["generic"],
    "fontsize": 12,
    "padding": 10,
}

bar: Bar = Bar(
    widgets=[
        *Logo(),
        Separator(),
        GroupBox(),
        *WindowName(),
        Systray(),
        Separator(),
        *Keyboard(),
        Wifi(),
        *Clock(),
    ],
    size=32,
    background=options["colour_scheme"]["background"],
    border_color=options["colour_scheme"]["background"],
    border_width=5,
    margin=[5, 10, 10, 10],
)
