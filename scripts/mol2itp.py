#!/usr/bin/env python
# This small script creates a mol2 file with the charges from the gromacs topology
# It prints the output file to the standard output
# Use chimera to convert the gro file to the mol2 format

import string
import re
import sys
import os
import math
#import numpy as np
if(len(sys.argv) != 4):
   print("Usage file.mol2 file.itp file.gro")
   exit()
MOL2 = sys.argv[1]
ITP  = sys.argv[2]
GRO  = sys.argv[3]
mol_f = open(MOL2,"r")
itp_f = open(ITP,"r")
gro_f = open(GRO,"r")
trash = gro_f.readline()
natoms = int(gro_f.readline())
gro_f.close()
#print(natoms)
#mol_lines = mol_f.readlines()
#itp_lines = itp_f.readlines()
#
#for line in itp_lines:
while True:
   line = itp_f.readline()
   #print(line[0:9])
   if line[0:9] == "[ atoms ]":
      itp_f.readline()
      break
#atoms = []
#charges = []
dict = {}
for f in range(natoms):
   line = itp_f.readline().split()
#   print(line)
   atom = line[4]
   charge = line[6]
   #print(atom,charge)
   dict[atom] = charge
#
#print(dict)
#
while True:
   line = mol_f.readline()
   if line[0:10] ==  "NO_CHARGES":
      line = "USER_CHARGES"
   print(line,end='')
   #print(line[0:13])
   if line[0:13] == "@<TRIPOS>ATOM":
      break
for f in range(natoms):
   line_o = mol_f.readline() 
   line = line_o.split()
   #print(line)
   atom = line[1]
   charge = dict[atom]
   #print(charge)
   linha=line_o[:-7]
   print(linha+charge)
lines =  mol_f.readlines()
for line in lines:
   print(line,end='')
