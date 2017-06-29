#!/usr/bin/env python
#分割POSIX的who命令输出

import os
import re

f = os.popen('who', 'r')
for eachLine in f:
    print(re.split(r'\s\s+|\t', eachLine.rstrip()))
f.close()