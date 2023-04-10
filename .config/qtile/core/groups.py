from libqtile.config import Group, Match

groups: list[Group] = [
    Group(
        name="1",
        matches=[Match(wm_class="code")],
        label="I",
    ),
    Group(
        name="2",
        matches=[Match(wm_class=["firefoxdeveloperedition", "chromium"])],  # type: ignore
        label="II",
    ),
    Group(
        name="3",
        matches=[Match(wm_class="discord")],
        label="III",
    ),
    Group(
        name="4",
        label="IV",
    ),
    Group(
        name="5",
        label="V",
    ),
    Group(
        name="6",
        label="VI",
    ),
    Group(
        name="7",
        label="VII",
    ),
    Group(
        name="8",
        label="VIII",
    ),
]
