import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ["assets/", 'inc/']

# TARGET
target = Executable(
    script="index.py",
    base="Win32GUI",
    # icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name="IceStore",
    version="1.0",
    description="Modern GUI for Python applications",
    author="mahmoud",
    options={'build_exe': {'include_files': files}},
    executables=[target]

)
