from qtile_extras import widget

from utils import options


def Text(
    text: str,
    background: str = options["colour_scheme"]["background"],
    padding: int = 1,
) -> object:
    return widget.TextBox(
        background=background,
        foreground=options["colour_scheme"]["foreground_light"],
        padding=padding,
        font=options["fonts"]["generic"],
        text=text,
    )
