# Arquivo para gerar o executável
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"],  "includes": ["PySide6"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="LuHf",
    version="1.0",
    description="U",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="main.py", base=base, icon="")]
)