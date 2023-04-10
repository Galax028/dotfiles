import json
from typing import TypedDict

from .variables import home


class OptionsApplications(TypedDict):
    app_launcher: str
    browser: str
    file_manager: str
    power_menu: str
    terminal: str
    window_switcher: str


class OptionsBar(TypedDict):
    keyboard_layouts: list[str]
    wifi_interface: str
    clock_format: str


class OptionsWallpaper(TypedDict):
    path: str
    mode: str


class OptionsFonts(TypedDict):
    generic: str
    icon: str


class OptionsColourScheme(TypedDict):
    background: str
    foreground_light: str
    foreground_dark: str
    border: str
    accent: str
    blue1: str
    blue2: str
    blue3: str
    red: str


class Options(TypedDict):
    applications: OptionsApplications
    bar: OptionsBar
    wallpaper: OptionsWallpaper
    fonts: OptionsFonts
    colour_scheme: OptionsColourScheme


default_options: Options = {
    "applications": {
        "app_launcher": "rofi -show drun",
        "browser": "firefox",
        "file_manager": "pcmanfm",
        "power_menu": "rofi -show power-menu -modi power-menu:rofi-power-menu",
        "terminal": "xterm",
        "window_switcher": "rofi -show window",
    },
    "bar": {
        "keyboard_layouts": ["us", "th"],
        "wifi_interface": "wlp45s0",
        "clock_format": "%I:%M %p - %d/%m/%Y",
    },
    "wallpaper": {
        "path": "",
        "mode": "fill",
    },
    "fonts": {
        "generic": "Fira Code Bold",
        "icon": "Ubuntu Nerd Font",
    },
    "colour_scheme": {
        "background": "#171717",
        "foreground_light": "#fafafa",
        "foreground_dark": "#0a0a0a",
        "border": "#404040",
        "accent": "#213f8c",
        "blue1": "#2563eb",
        "blue2": "#1d4ed8",
        "blue3": "#1e40af",
        "red": "#b91c1c",
    },
}

try:
    with open(f"{home}/.config/qtile/options.json", "r") as f:
        options: Options = json.load(f)
except FileNotFoundError:
    options = default_options.copy()
