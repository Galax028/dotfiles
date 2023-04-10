from libqtile.config import Key
from libqtile.lazy import lazy

from utils import alt, ctrl, mod, options, shift, take_screenshot

keys: list[Key] = [
    # Application spawning
    Key([mod], "s", lazy.spawn(options["applications"]["app_launcher"]), desc="Launch app launcher"),
    Key([mod], "e", lazy.spawn(options["applications"]["file_manager"]), desc="Launch file manager"),
    Key([mod], "f", lazy.spawn(options["applications"]["browser"]), desc="Launch browser"),
    Key([mod], "Return", lazy.spawn(options["applications"]["terminal"]), desc="Launch terminal"),

    # Window management
    Key([mod, ctrl], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, ctrl], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, ctrl], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, ctrl], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([alt], "Return", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, shift], "q", lazy.window.kill(), desc="Kill focused window"),

    # Window switching
    Key([mod], "h", lazy.layout.left(), desc="Move focus to the left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.spawn(options["applications"]["window_switcher"]), desc="Launch window switcher"),

    # Group switching
    Key([alt], "Tab", lazy.screen.next_group(), desc="Switch to next group"),
    Key([alt, "shift"], "Tab", lazy.screen.prev_group(), desc="Switch to previous group"),

    # Function keys
    Key([], "XF86AudioLowerVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 10%-"), desc="Lower volume by 10%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 10%+"), desc="Raise volume by 10%"),

    # Miscellaneous
    Key([mod], "Print", lazy.function(take_screenshot), desc="Take a screenshot"),
    Key([], "Print", lazy.function(take_screenshot, False), desc="Take a screenshot (area)"),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Change keyboard layout"),
    Key([mod, ctrl], "r", lazy.reload_config(), desc="Reload the config"),
]

for i in range(1, 9):
    keys.extend(
        [
            Key([mod],
                str(i),
                lazy.group[str(i)].toscreen(),
                desc=f"Switch to group {i}",
            ),
            Key(
                [mod, "shift"],
                str(i),
                lazy.window.togroup(str(i), switch_group=True),
                desc=f"Switch and move focused window to group {i}",
            ),
        ]
    )
