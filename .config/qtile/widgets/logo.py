from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from utils import options

from .icon import Icon

decorations: list = [
    RectDecoration(
        filled=True,
        line_width=0,
        padding_y=2,
        radius=18,
        use_widget_background=True,
    ),
]


def Logo() -> tuple[object, object]:
    return (
        Icon(
            icon="    ",
            background=options["colour_scheme"]["accent"],
            decorations=decorations,
            padding=15,
            mouse_callbacks={
                "Button1": lazy.spawn(options["applications"]["power_menu"]),
            },
        ),
        widget.Spacer(length=3),
    )
