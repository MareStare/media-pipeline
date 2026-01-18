from krita import Krita, InfoObject
import os

app = Krita.instance()
doc = app.activeDocument()

if doc is None:
    raise RuntimeError("No active document")

kra_path = doc.fileName()
if not kra_path:
    raise RuntimeError("Document has not been saved yet")

base, _ = os.path.splitext(kra_path)
out_path = base + ".png"

params = InfoObject()
params.setProperty("compression", 9)
params.setProperty("indexed", False)
params.setProperty("interlaced", False)

params.setProperty("saveSRGBProfile", False)
params.setProperty("forceSRGB", False)
params.setProperty("alpha", True)
params.setProperty("transparencyFillcolor", [0, 0, 0])

doc.exportImage(out_path, params)


window = app.activeWindow()
view = window.activeView()
if view is not None:
    view.showFloatingMessage("Hi!", app.icon("document-save-as"), 2000, 1)
