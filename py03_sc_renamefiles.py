#################################################################################
# TITLE:            Bulk Renaming Program                                       #
# AUTHOR:           BASASKS                                                     #
# PYTHON VERSION:   Python 3.5.9                                                #
# USAGE:            python3 py03_sc_renamefiles.py                              #
# NOTES:            1. Modify all static variables per requirements             #
#                   2. No sorting requirement for files                         #
# ASSUMPTIONS:      1. All files in directory will be renamed                   #
#                   2. File extension with be string succeeding last period     #
# FOR ENHANCEMENTS: 1. Sort file according to last modified timestamp           #
#                   2. Rename only file for cetain extension type               #
#################################################################################

import os
from pathlib import Path

# STATIC VARIABLES
filepath = "/home/basasks/input/py03/"
fileprefix = "testprefix_"
counter = 1

def renamefile(nameold):
    global counter
    fileext = Path(nameold).suffix
    filectr = str(counter).zfill(4)
    namenew = fileprefix + filectr + fileext
    os.rename(filepath+nameold, filepath+namenew)
    counter += 1

# LOOP THROUGH ALL FILES IN FOLDER
filearray = os.listdir(filepath)
for t_filename in enumerate(filearray):
    filename = t_filename[1]
    renamefile(filename)
    
    
