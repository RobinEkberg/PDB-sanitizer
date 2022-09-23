from cgitb import reset
import os
from urllib import response
import requests

amino_acids = ['ALA ', 'ARG ', 'ASN ', 'ASP ', 'CYS ', 'GLU ', 'GLN ', 'GLY ', 'HIS ', 'ILE ',
               'LEU ', 'LYS ', 'MET ', 'PHE ', 'PRO ', 'SER ', 'THR ', 'TRP ', 'TYR ', 'VAL ', 'HOH ']
arg = ['ATOM', 'ANISOU', 'TER ']
arg_water = ['ATOM', 'ANISOU', 'TER ', 'HETATM']




input_structure = input('Enter .pdb-ID:')

URL = (f'https://files.rcsb.org/download/{input_structure}.pdb')
downloaded_pdb = requests.get(URL)


input_pdb = (f'{input_structure}.pdb')

open(f'{input_pdb}', 'wb').write(downloaded_pdb.content)


fname = os.path.splitext(input_pdb)
input_water = input('Keep water? ')

def sanitation(input_pdb, input_water):
    with open(f'{input_pdb}', 'rt') as f:
        input_pdb_data = f.readlines()

    new_pdb = []

    for line in input_pdb_data:
        if input_water == 'No':
            for i in arg:
                for a in amino_acids:
                    if i in line:
                        if a in line:
                            
                            new_pdb.append(line)


        else:
            for i in arg_water:
                for a in amino_acids:
                    if i in line:
                        if a in line:
                            #print(line)
                            new_pdb.append(line)

    return new_pdb



out_pdb = (fname[0]+'_sanitized'+fname[1])

sanitized_pdb = sanitation(input_pdb, input_water)
clean_pdb = open(f'{out_pdb}', 'w')

for i in sanitized_pdb:
    clean_pdb.write(i)

clean_pdb.close()

if input_water == 'No':
    print('The file was sanitized and water was removed form the crystal structure')
if input_water != 'No':
    print('The file was sanitized and water was kept in the crystal structure')