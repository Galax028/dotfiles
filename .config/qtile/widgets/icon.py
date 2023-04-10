from qtile_extras import widget

from utils import options


def Icon(
    icon: str,
    background: str = options["colour_scheme"]["background"],
    decorations: list | None = None,
    padding: int = 1,
    mouse_callbacks: dict | None = None
) -> object:
    return widget.TextBox(
        background=background,
        foreground=options["colour_scheme"]["foreground_light"],
        decorations=decorations,
        padding=padding,
        font=options["fonts"]["icon"],
        fontsize=18,
        text=icon,
        mouse_callbacks=mouse_callbacks,
    )
