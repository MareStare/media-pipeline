from krita import *

Krita.instance().action("KritaShape/KisToolBrush").trigger()
Krita.instance().action("activate_preset_2").trigger()
Krita.instance().activeWindow().activeView().setBrushSize(3.5)
Krita.instance().action("set_simple_brush_smoothing").trigger()
