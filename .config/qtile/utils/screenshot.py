from libqtile.core.manager import Qtile

from .variables import home


def take_screenshot(qtile: Qtile, fullscreen: bool = True) -> None:
    if fullscreen:
        qtile.cmd_spawn(f"bash {home}/.config/qtile/utils/screenshot_full.sh")
        return

    qtile.cmd_spawn(f"bash {home}/.config/qtile/utils/screenshot_region.sh")
