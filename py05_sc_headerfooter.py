#################################################################################
# TITLE:            Header-Footer Program for File Conversion                   #
# AUTHOR:           BASASKS                                                     #
# PYTHON VERSION:   Python 3.5.9                                                #
# USAGE:            python3 py05_sc_headerfooter.py                             #
# DEV NOTES:        1. Use Case: Append header and footer to a file, with some  #
#                       file specific placeholders on header                    #
#                   2. Works only for one time run as it overwrites             #
#                       original file on same directory                         #
#                   3. Hard-coded values under variable declarations (con_*)    #
#################################################################################


#####  MODULES

import os
import re
import glob


#####  VARIABLES DECLARATIONS

con_path = "/home/basasks/input/py05/"
con_ext = "sh"
con_header = "/home/basasks/input/py05/in_header.txt"
con_footer = "/home/basasks/input/py05/in_footer.txt"
con_params = "/home/basasks/input/py05/in_params.txt"
lst_fullnames = []
dct_params = {}


#####  CHECK STATIC VALUES

# Check if directory exists
if not os.path.isdir(con_path):
    print("Error: File path does not exist")
    exit(1)

# Check if there are files to process
if len(glob.glob(con_path + "*." + con_ext)) <= 0:
    print("Warning: No files to process")
    exit(0)

# Check header, footer, and parameter files
if not os.path.isfile(con_header):
    print("Error: Header file does not exist")
    exit(1)
if not os.path.isfile(con_footer):
    print("Error: Footer file does not exist")
    exit(1)
if not os.path.isfile(con_params):
    print("Error: Parameter file does not exist")
    exit(1)


#####  STORE PARAMETER FILE TO DICTIONARY

with open(con_params) as f:
    for line in f:
        olddb = line.split('|')[0].strip()
        newdb = line.split('|')[1].strip()
        dct_params[olddb] = newdb


#####  STORE ALL FILES TO BE MODIFIED TO LIST

for filename in os.listdir(con_path):
    if filename.endswith(con_ext): 
        lst_fullnames.append(os.path.join(con_path, filename))
        continue
    else:
        continue
        
        
#####  PROCESS EACH FILE IN LIST

filename = ""
for filename in lst_fullnames:

    # PREPARATION
    rep_scriptname = filename
    rep_usage = "sh " + rep_scriptname
    newfilename = rep_scriptname + "_tmp"
    if os.path.exists(newfilename):
        os.remove(newfilename)

    # WRITE HEADER
    f_new = open(newfilename, "w")
    with open(con_header) as f:
        for line in f:
            newline = line
            newline = re.sub("_PLACEHOLDER_SCRIPTNAME_", rep_scriptname, newline)
            newline = re.sub("_PLACEHOLDER_USAGE_", rep_usage, newline)
            f_new.write(newline)
        f_new.write("\n")
    f_new.close()
        
    # WRITE BODY
    f_new = open(newfilename, "a")
    with open(filename) as f:
        for line in f:
            newline = line
            for key in dct_params:
                newline = re.sub(key, dct_params[key], newline)
            f_new.write(newline)
        f_new.write("\n")
    f_new.close()

    # WRITE FOOTER
    f_new = open(newfilename, "a")
    with open(con_footer) as f:
        for line in f:
            f_new.write(line)
        f_new.write("\n")
    f_new.close()

    # DELETE-RENAME FILE
    if os.path.exists(filename):
        os.remove(filename)
    os.rename(newfilename, filename)