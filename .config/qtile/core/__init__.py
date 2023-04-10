from . import hooks
from .bar import bar, defaults
from .groups import groups
from .keys import keys
from .layouts import floating_layout, layouts
from .mouse import mouse
from .screen import screens

extension_defaults: dict[str, object] = defaults.copy()
widget_defaults: dict[str, object] = defaults.copy()

__all__ = [
    "bar",
    "extension_defaults",
    "floating_layout",
    "groups",
    "hooks",
    "keys",
    "layouts",
    "mouse",
    "widget_defaults",
    "screens",
]
