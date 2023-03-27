#using pathlib .path.mkdir

from pathlib import Path
Path("/root/dirA/dirB").mkdir(parents=True, exist_ok=True)

# using os.makedirs function

import os
os.makedirs("/root/dirA/dirB")


# using distutils.dir_util

import distutils.dir_util
distutils.dir_util.mkpath("/root/dirA/dirB")

# Raising and exception if directory already exists

import os
try:
    os.makedirs("/dirA/dirB")
except FileExistsError:
    print("File already exists")
