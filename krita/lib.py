from krita import *
import os

# Defaults
default_size = 4
default_smooth = None

brushes = {
    "eraser": {
        "preset": "1",
        "size": None,
        "smooth": None,
    },
    "1": {
        "preset": "2",
        "size": None,
        "smooth": None,
    },
    "2": {
        "preset": "3",
        "size": None,
        "smooth": None,
    },
    "3": {
        "preset": "4",
        "size": None,
        "smooth": False,
    },
    "4": {
        "preset": "5",
        "size": None,
        "smooth": False,
    },
}


def run(script_path: str):
    global default_size, default_smooth, brushes

    brush_name = os.path.basename(script_path)

    brush_name = brush_name.replace("script-", "").replace(".py", "")
    brush = brushes.get(brush_name)

    if brush is None:
        raise ValueError(f"Unknown brush: {brush_name}")

    app = Krita.instance()

    app.action("KritaShape/KisToolBrush").trigger()
    app.action(f"activate_preset_{brush['preset']}").trigger()

    size = brush.get("size", default_size)
    if size is not None:
        app.activeWindow().activeView().setBrushSize(size)

    smooth = brush.get("smooth", default_smooth)
    if smooth is not None:
        if smooth:
            app.action("set_stabilizer_brush_smoothing").trigger()
        else:
            app.action("set_simple_brush_smoothing").trigger()
