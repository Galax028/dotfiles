from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

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
]


def Clock() -> tuple[object, object, object]:
    return (
        Icon(
            icon="    ",
            background=options["colour_scheme"]["blue3"],
            decorations=decorations,
            padding=0,
        ),
        widget.Clock(
            background=options["colour_scheme"]["blue3"],
            foreground=options["colour_scheme"]["foreground_light"],
            decorations=decorations,
            padding=0,
            font=options["fonts"]["generic"],
            fmt="{}  ",
            format=options["bar"]["clock_format"],
        ),
        widget.Spacer(length=6),
    )
