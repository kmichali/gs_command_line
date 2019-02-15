#!/usr/bin/env python

import os
import sys
import re


if len(sys.argv)!= 3:
   print("usage: filter.py intput output")
   quit()

fin = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
for line in fin:
   if not re.match(r'^\s*$',line):
      fout.write(line)

fin.close()
fout.close()
     


