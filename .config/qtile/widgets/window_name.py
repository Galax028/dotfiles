from libqtile.bar import CALCULATED
from qtile_extras import widget


def WindowName() -> tuple[object, object, object]:
    return (
        widget.Spacer(),
        widget.WindowName(width=CALCULATED),
        widget.Spacer(),
    )
