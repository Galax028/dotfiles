from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration

from utils import options

from .icon import Icon

decorations: list = [
    RectDecoration(
        filled=True,
        group=True,
        line_width=0,
        padding_y=2,
        radius=18,
        use_widget_background=True,
    ),
    PowerLineDecoration(
        padding_y=1,
        path="arrow_right",
    ),
]


def Wifi() -> object:
    return widget.WiFiIcon(
        background=options["colour_scheme"]["blue2"],
        foreground=options["colour_scheme"]["foreground_light"],
        active_colour=options["colour_scheme"]["foreground_light"],
        inactive_colour=options["colour_scheme"]["border"],
        decorations=decorations,
        padding=8,
        font=options["fonts"]["generic"],
        interface=options["bar"]["wifi_interface"],
    )
