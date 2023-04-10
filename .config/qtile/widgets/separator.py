from qtile_extras import widget

from utils import options


def Separator() -> object:
    return widget.TextBox(
        background=options["colour_scheme"]["background"],
        foreground=options["colour_scheme"]["border"],
        padding=5,
        font=options["fonts"]["generic"],
        fontsize=20,
        text="•",
    )
