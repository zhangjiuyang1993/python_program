#!/usr/bin/env python
#处理DOS环境下的tasklist命令的输出

import os
import re

f = os.popen('tasklist /nh', 'r')
for eachLine in f:
    print(re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+K)', eachLine.rstrip()))
f.close()