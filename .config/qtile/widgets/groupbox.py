from qtile_extras import widget

from utils import options


def GroupBox() -> object:
    return widget.GroupBox(
        active=options["colour_scheme"]["foreground_light"],
        background=options["colour_scheme"]["background"],
        foreground=options["colour_scheme"]["foreground_light"],
        highlight_color=[
            options["colour_scheme"]["background"],
            options["colour_scheme"]["border"],
        ],
        inactive=options["colour_scheme"]["border"],
        this_current_screen_border=options["colour_scheme"]["accent"],
        this_screen_border=options["colour_scheme"]["accent"],
        urgent_border=options["colour_scheme"]["red"],
        urgent_text=options["colour_scheme"]["red"],
        rounded=False,
        font=options["fonts"]["generic"],
        highlight_method="line",
        urgent_alert_method="line",
    )
