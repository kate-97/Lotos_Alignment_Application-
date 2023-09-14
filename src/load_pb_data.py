# Implementations of functions for loading data from PDB database and
# transformation of 3D structure data into format of PB sequences

# necessary imports
import os, pathlib
import read_config_data as rcd

# removing 'Z' characters from begin and end of PB sequence
def transform_seq_line(seq):
    seq = seq.strip()
    seq = seq.rstrip()
    while seq[0] == 'Z':
        seq = seq[1:]

    while seq[-1] == 'Z':
        seq = seq[:-1]

    return seq

# converts PDB from file on path PDBFilePath into PB format and saves this into
# FASTA file whose path is returned
def convertPDBToPB(PDBFilePath):
    currentPath = os.getcwd()
    FASTA_DIRECTORY = rcd.get_path('FASTA_FILES_DIRECTORY')

    pos = PDBFilePath.rindex(".")
    pos1 = PDBFilePath[:pos].rindex("/")
    pdb_id = PDBFilePath[pos1 + 1:pos]
    fasta_name = pdb_id + ".PB.fasta"
    fasta_path = os.path.join(FASTA_DIRECTORY, fasta_name)

    if os.path.exists(fasta_path):
        return fasta_path

    os.chdir(FASTA_DIRECTORY)

    commandPBXplore = "PBassign -p " + PDBFilePath + " -o " + pdb_id
    os.system(commandPBXplore)
    os.chdir(currentPath)

    fasta_name = pdb_id + ".PB.fasta"
    fasta_path = os.path.join(FASTA_DIRECTORY, fasta_name)
    return fasta_path

# loading pdb from PDB database and transformation of 3D data from PDB file
# into PB format
def load_pb_format(pdb_id):
    pdbFileName = pdb_id + ".pdb"
    PDB_DIRECTORY = rcd.get_path('PDB_FILES_DIRECTORY')
    pathPdbFileName = os.path.join(PDB_DIRECTORY, pdbFileName)

    if not os.path.exists(pathPdbFileName):
        commandDownload = "wget -P " + PDB_DIRECTORY + " https://files.rcsb.org/view/"
        commandDownload += pdbFileName
        os.system(commandDownload)

    currentPath = os.getcwd()
    FASTA_DIRECTORY = rcd.get_path('FASTA_FILES_DIRECTORY')
    fasta_name = pdb_id + ".PB.fasta"
    fasta_path = os.path.join(FASTA_DIRECTORY, fasta_name)

    if os.path.exists(fasta_path):
        return fasta_path

    os.chdir(FASTA_DIRECTORY)

    commandPBXplore = "PBassign -p " + pathPdbFileName + " -o " + pdb_id
    os.system(commandPBXplore)
    os.chdir(currentPath)

    fasta_name = pdb_id + ".PB.fasta"
    fasta_path = os.path.join(FASTA_DIRECTORY, fasta_name)
    return fasta_path


# function which passes through collection composed of pdb id-s, pdb files and
# fasta files (with pb sequences) and finds pb sequences for proteins with pdb id-s or from pdb-s
# and store them into fasta files
def generate_fastas(sources):
    fasta_files = []

    for source in sources:
        if source[1] == 'fasta':
            fasta_files.append(source[0])

        if source[1] == 'id':
            fasta_path = load_pb_format(source[0])
            fasta_files.append(fasta_path)

        if source[1] == 'pdb':
            fasta_path = convertPDBToPB(source[0])
            fasta_files.append(fasta_path)

    return fasta_files