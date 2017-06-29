#!usr/bin/env python
#rewho.py的Python3的版本

import os
import re

with os.popen('who', 'r') as f:
    for eachLine in f:
        print(re.split(r'\s\s+|\t', eachLine.strip()))