import ctypes
import os
import sys

def recurso(nombre):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, nombre)

imagen = recurso("wall.jpg")

if os.path.exists(imagen):
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, imagen, 3
    )
