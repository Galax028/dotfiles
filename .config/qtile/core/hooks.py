import subprocess

from libqtile import hook

from core.bar import bar
from utils import home


@hook.subscribe.startup_once
def startup_once() -> None:
    subprocess.Popen([f"{home}/.config/qtile/autostart.sh"])


@hook.subscribe.startup
def startup() -> None:
    bar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)  # type: ignore
