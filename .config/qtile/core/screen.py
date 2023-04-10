from os import path

from libqtile.bar import Gap
from libqtile.config import Screen

from core.bar import bar
from utils import options

screens: list[Screen] = [
    Screen(
        wallpaper=path.expanduser(options["wallpaper"]["path"]),
        wallpaper_mode=options["wallpaper"]["mode"],
        top=Gap(size=5),
        bottom=bar,
        left=Gap(size=5),
        right=Gap(size=5),
    ),
]
