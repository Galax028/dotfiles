from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration

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


def Keyboard() -> tuple[object, object]:
    return (
        Icon(
            icon="   ",
            background=options["colour_scheme"]["blue1"],
            decorations=decorations,
            padding=0,
        ),
        widget.KeyboardLayout(
            background=options["colour_scheme"]["blue1"],
            foreground=options["colour_scheme"]["foreground_light"],
            decorations=decorations,
            padding=0,
            font=options["fonts"]["generic"],
            fmt="{} ",
            configured_keyboards=options["bar"]["keyboard_layouts"],
        ),
    )
