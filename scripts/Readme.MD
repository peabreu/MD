Various scripts for use with gromacs files:

- mol2itp.py
This file reads a mol2, gro and itp files and prints to the standard output a new mol2 file with the charges from the itp file.
Use UCSF Chimera to read and convert the gro file to mol2.
Then use the script as : ./mol2itp.py file.mol2 file.itp file.gro | tee new_file.mol2
