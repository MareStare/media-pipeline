from krita import *
import os

# Defaults
sizes = {
    "1": 60,
    "2": 30,
    "3": 10,
}

default_smooth = None

brush_presets: dict[str, dict[str, str | bool | None]] = {
    "1": {
        "preset": "3",
        "size": None,
        "smooth": None,
    },
    "2": {
        "preset": "4",
        "size": None,
        "smooth": None,
    },
    "3": {
        "preset": "5",
        "size": None,
        "smooth": False,
    },
    "4": {
        "preset": "6",
        "size": None,
        "smooth": False,
    },
}


def run(script_path: str):
    global default_size, default_smooth, brush_presets, sizes

    tool_name = os.path.basename(script_path)

    tool_name = tool_name.replace("script-", "").replace(".py", "")

    app = Krita.instance()

    if tool_name.startswith("brush-size"):
        size_key = tool_name.replace("brush-size-", "")
        size = sizes.get(size_key)
        if size is None:
            raise ValueError(f"Unknown brush size: {size_key}")

        app.activeWindow().activeView().setBrushSize(size)
        return

    if tool_name == "fill":
        app.action("KritaFill/KisToolFill").trigger()
        app.action("erase_action").setChecked(False)
        return

    if tool_name.startswith("eraser"):
        if get_active_tool() == "KritaFill/KisToolFill":
            app.action("erase_action").setChecked(True)
            return

        app.action("KritaShape/KisToolBrush").trigger()

        brush_number = 1 if tool_name == "eraser-hard" else 2

        app.action(f"activate_preset_{brush_number}").trigger()
        app.action("set_simple_brush_smoothing").trigger()
        return

    app.action("KritaShape/KisToolBrush").trigger()
    app.action("erase_action").setChecked(False)

    brush = brush_presets.get(tool_name)

    if brush is None:
        raise ValueError(f"Unknown brush: {tool_name}")

    preset = brush.get("preset")
    if preset is not None:
        app.action(f"activate_preset_{preset}").trigger()

    # size = brush.get("size", default_size)
    # if size is not None:
    #     app.activeWindow().activeView().setBrushSize(size)

    smooth = brush.get("smooth", default_smooth)
    if smooth is not None:
        if smooth:
            app.action("set_stabilizer_brush_smoothing").trigger()
        else:
            app.action("set_simple_brush_smoothing").trigger()


# Taken from https://krita-artists.org/t/active-tool-request/78904/2
def get_active_tool():
    dockers = Krita.instance().dockers()
    qdock = next((w for w in dockers if w.objectName() == "ToolBox"), None)
    wobj = qdock.findChild(QButtonGroup)
    return wobj.checkedButton().objectName()
