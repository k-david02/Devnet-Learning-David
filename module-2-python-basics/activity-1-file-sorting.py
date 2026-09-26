"""
Module 2 — Activity: File Sorting with os and shutil
Student: [your name]
Date: [date]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[is sorts images into folder that ONLY accept image file]


============================================
KEY VOCABULARY
============================================
- os module: this is a python module that lets us work with files and folder
- shutil module: use to copy and move files with os module
- file path: location of a fike
- directory: ending of a file name
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# --- paste your existing code here ---
older = "my_files"

for file in os.listdir(folder):
    if file.endswith(".jpg"):
        shutil.move(folder + "/" + file, folder + "/Images/" + file)
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[One mistake I want to avoid is using the wrong folder name or file
path. If Python cannot find the folder, the program will give an
error. I also need to be careful when moving files because I do not
want to accidentally move the wrong file ]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
