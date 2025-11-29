from krita import *

Krita.instance().action("KritaShape/KisToolBrush").trigger()
Krita.instance().action("activate_preset_4").trigger()
Krita.instance().action("set_simple_brush_smoothing").trigger()
