from qtile_extras import widget

from utils import options


def Systray() -> object:
    return widget.Systray(
        background=options["colour_scheme"]["background"],
        padding=2,
    )
