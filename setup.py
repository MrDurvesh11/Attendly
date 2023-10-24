import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"D:\python 3.8.5\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"D:\python 3.8.5\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Attendence System Using Face Recognition",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'images','data','database','Attendance_csv']}},
    version = "1.0",
    description = "Attendence System Using Face Recognition | Developed By Coders",
    executables = executables
    )
