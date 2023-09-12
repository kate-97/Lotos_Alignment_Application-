# Implementations of functions for loading data from PDB database and
# transformation of 3D structure data into format of PB sequences

# necessary imports
import os

# removing 'Z' characters from begin and end of PB sequence
def transform_seq_line(seq):
    seq = seq.strip()
    seq = seq.rstrip()
    while seq[0] == 'Z':
        seq = seq[1:]

    while seq[-1] == 'Z':
        seq = seq[:-1]

    return seq


# loading pdb from PDB database and transformation of 3D data from PDB file
# into PB format
def load_pb_format(pdb_id):
    commandDownload = "wget https://files.rcsb.org/view/"
    commandDownload += pdb_id + ".pdb"
    os.system(commandDownload)

    commandPBXplore = "PBassign -p " + pdb_id + ".pdb -o " + pdb_id
    os.system(commandPBXplore)
    path_content = pdb_id + ".PB.fasta"
    ''' absolutePath = os.path.abspath(path_content)
    
    fileFASTA = open(absolutePath, "r")
    if not fileFASTA:
        print("Neuspesno otvaranje")
    else:
        print("Uspesno otvaranje")
    fileFASTA.close()
    '''
