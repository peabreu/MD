#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Paulo E. Abreu (c) 2008 Departamento de Química, Universidade de Coimbra, Portugal
# This is free software.  You may redistribute it under the terms
# of the Apache license and the GNU General Public License Version
# 2 or at your option any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Contributor(s):
#
# Description:
# Orders an arbitrary gro file according to a template gro file
#
#
#
########################################################################################
########################################################################################
########################################################################################
import os
import sys
import re
import string
from math import *
# parse command line arguments
args = sys.argv[1:]
nargs = len(args)
if nargs != 1:
        print('Specify one "file.gro"')
        sys.exit()
filename = args[0]

# Reads the file to be ordered
lines1 = []
with open(filename) as f1:
    lines1 = f1.readlines()
# Reads the template used as a template for the ordering
lines2 = []
with open('IMD.gro') as f2:
    lines2 = f2.readlines()

# write the two initial lines
print(lines1[0],end='')
print(lines1[1],end='')

# save the last line of the gro files
lastline1=lines1[-1]
lastline2=lines2[-1]

# remove the two first lines + the last line
lines1=lines1[2:-1]
lines2=lines2[2:-1]

for line in lines2:
    words=line.split()
    ATOM=words[2]
    # find line containing ATOM in the file to be ordered
    for line1 in lines1:
        found_atom=0
        words1=line1.split()
        word=words1[1]
        if word == ATOM:
           print(line1,end='')
           found_atom=1
           break
    if found_atom==0:
       print("atom not found:",word)
print(lastline1,end='')

