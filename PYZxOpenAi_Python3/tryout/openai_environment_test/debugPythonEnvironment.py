'''
Sicherstellen, dass das endcoding passt, etc. 

Created on 04.11.2026

@author: Fritz Lindhauer
'''

import sys
import locale
import os

print("Python-Version:", sys.version)
print("Standard-Encoding:", sys.getdefaultencoding())
print("Filesystem-Encoding:", sys.getfilesystemencoding())
print("Locale-Encoding:", locale.getpreferredencoding(False))

print("stdout-Encoding:", sys.stdout.encoding)
print("stderr-Encoding:", sys.stderr.encoding)

print("PYTHONIOENCODING:", os.environ.get("PYTHONIOENCODING"))
print("PYTHONUTF8:", os.environ.get("PYTHONUTF8"))
