# Implementations of functions for loading PB sequences, their multiple alignment and generating textual report

# necessary imports
import sys

import biotite
import biotite.sequence as sequence
import biotite.sequence.align as alignment
import biotite.sequence.graphics as graphics
from biotite.sequence.io import fasta
from matplotlib import pyplot as plt
import seaborn

import load_pb_data


# NOTE: This piece of code for substitution matrix is taken from source:
# https://www.biotite-python.org/examples/gallery/structure/pb_alignment.html?highlight=protein+block .
##################################################################################
pb_alphabet = sequence.Alphabet(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])

# PB substitution matrix, adapted from PBxplore
matrix_str = """
    a     b     c     d     e     f     g     h     i     j     k     l     m     n     o     p
a  516   -59   113  -105  -411  -177   -27  -361    47  -103  -644  -259  -599  -372  -124   -83
b  -59   541  -146  -210  -155  -310   -97    90   182  -128   -30    29  -745  -242  -165    22
c  113  -146   360   -14  -333  -240    49  -438  -269  -282  -688  -682  -608  -455  -147     6
d -105  -210   -14   221     5  -131  -349  -278  -253  -173  -585  -670 -1573 -1048  -691  -497
e -411  -155  -333     5   520   185   186   138  -378   -70  -112  -514 -1136  -469  -617  -632
f -177  -310  -240  -131   185   459   -99   -45  -445    83  -214   -88  -547  -629  -406  -552
g  -27   -97    49  -349   186   -99   665   -99   -89  -118  -409  -138  -124   172   128   254
h -361    90  -438  -278   138   -45   -99   632  -205   316   192  -108  -712  -359    95  -399
i   47   182  -269  -253  -378  -445   -89  -205   696   186     8    15  -709  -269  -169   226
j -103  -128  -282  -173   -70    83  -118   316   186   768   196     5  -398  -340  -117  -104
k -644   -30  -688  -585  -112  -214  -409   192     8   196   568   -65  -270  -231  -471  -382
l -259    29  -682  -670  -514   -88  -138  -108    15     5   -65   533  -131     8   -11  -316
m -599  -745  -608 -1573 -1136  -547  -124  -712  -709  -398  -270  -131   241    -4  -190  -155
n -372  -242  -455 -1048  -469  -629   172  -359  -269  -340  -231     8    -4   703    88   146
o -124  -165  -147  -691  -617  -406   128    95  -169  -117  -471   -11  -190    88   716    58
p  -83    22     6  -497  -632  -552   254  -399   226  -104  -382  -316  -155   146    58   609
"""

def create_matrix():
    matrix_dict = alignment.SubstitutionMatrix.dict_from_str(matrix_str)
    matrix = alignment.SubstitutionMatrix(pb_alphabet, pb_alphabet, matrix_dict)
    return matrix


matrix_substitution = create_matrix()
##################################################################################


# utility function for printing textual reports
# checks if current character from alignment is gap and returns '-' in this case
def if_None(a):
    if a is None:
        return '-'
    else:
        return a


# utility function for name compress
def decrease_name_size(name):
    ind = name.rindex('|')
    s = name[ind+1:]
    print(s)
    dind = s.find(' ')
    print(s[:dind])
    return s[:dind]


# utility constants
LENGTH_HEADER = 25
BREAK_LENGTH = 50

# function for reading PB sequences from FASTA files
def read_sequences_from_fasta(path):
    names = []
    sequences = []


    fasta_file = fasta.FastaFile.read(path)
    for name, sequence in fasta_file.items():
        names.append(name)

        sequence = load_pb_data.transform_seq_line(sequence)
        if 'Z' in sequence:
            print(name + ": Unvalid PB sequence.", file=sys.stderr)
            return None

        sequences.append(sequence)

    return [names, sequences]


# function for generating textual report of multiple PB alignment
def generate_multi_alignment_report(align, pb_sequences, labels, distance_matrix, tree, output_file=True):
    lines = []
    lines.append("*****************")
    labels_formated = [decrease_name_size(l) for l in labels]
    m = len(align[0])
    n = len(align)
    codes = alignment.get_codes(align)
    line = 'Duzina poravnanja: ' + str(n)
    lines.append(line)
    matched = 0
    for i in range(0, n):
        ind = True
        for j in range(1, m):
            if codes[0][i] != codes[j][i]:
                ind = False
                break
        if ind:
            matched += 1

    line = 'Broj poklopljenih: ' + str(matched)
    lines.append(line)
    line = 'Alignment score: ' + str(
        alignment.score(align, matrix=alignment.SubstitutionMatrix.std_protein_matrix()))
    lines.append(line)

    aligned_sequences = alignment.get_symbols(align)
    # blank_spaces = max([len(a) for a in annotated_sequences[0]])
    # blank_spaces += 1
    blank_spaces = 40
    position = 0

    while position < n:
        position2 = position + BREAK_LENGTH
        if position2 > n:
            position2 = n

        for i in range(m):
            line = ''
            seq_name = ''
            if len(labels_formated[i]) < LENGTH_HEADER:
                seq_name = labels_formated[i]
            else:
                seq_name = labels_formated[i][:LENGTH_HEADER]
            line += seq_name
            n1 = len(seq_name)
            razmak =''.join([' ']*(blank_spaces - n1))
            line += razmak
            aligned_sequence = ''.join([if_None(e) for e in aligned_sequences[i][position:position2]])
            line += aligned_sequence
            lines.append(line)

        codes = alignment.get_codes(align)
        line = ''.join([' ']*(blank_spaces))

        for i in range(position, position2):
            ind = True
            for j in range(1, m):
                if codes[0][i] != codes[j][i]:
                    ind = False
                    break
            if ind:
                line += '*'
            else:
                line += ' '

        lines.append(line)
        lines.append('')
        position += BREAK_LENGTH

    line = "Guide tree:"
    lines.append(line)
    line = str(tree.to_newick(labels=labels_formated, include_distance=False))
    lines.append(line)
    line = "Profile matrix:"
    lines.append(line)
    profile_matrix = [list(r) for r in ((sequence.SequenceProfile.from_alignment(align)).symbols)]
    lines.append(str(profile_matrix))
    line = "Matrix of calculated distances between sequences:"
    lines.append(line)
    lines.append(str(distance_matrix))
    return lines


# function for executing multiple PB alignment and generating textual report of this alignment
def execute_alignment_and_generate_report(pdbs):
    fasta__files = []
    for pdb in pdbs:
        load_pb_data.load_pb_format(pdb)
        fasta__files.append(pdb + ".PB.fasta")

    sequences = []
    labels = []
    for fasta__f in fasta__files:
        results = read_sequences_from_fasta(fasta__f)
        if results is None:
            return None

        labels += (results[0])
        sequences += (results[1])

    sequences_pb = [sequence.GeneralSequence(pb_alphabet, sequence=s)
                    for s in sequences]

    align, order, tree, distance_matrix = alignment.align_multiple(sequences_pb,
                                                                   matrix=matrix_substitution)
    alignment_data = {}
    alignment_data['alignment'] = align
    alignment_data['order'] = order
    alignment_data['tree'] = tree
    alignment_data['distance_matrix'] = distance_matrix
    lines = generate_multi_alignment_report(align, sequences, labels, distance_matrix, tree)
    return labels, alignment_data, lines