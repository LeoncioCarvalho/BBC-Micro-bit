import machine
import os
from usys import *
import antigravity
import love
import this
print(this.authors())
print("Unique_ID      : ", machine.unique_id())
print("Frequency      : ", machine.freq(),"Hz")
print("SYS  Info      : ", os.uname())
print("Platform       : ", platform)
print("Version        : ", version)
print("Version_Info   : ", version_info)
print("Path           : ", path)
