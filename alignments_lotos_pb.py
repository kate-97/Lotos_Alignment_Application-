# Implementations of functions for loading PB sequences, their pairwise alignment and generating textual report

# necessary imports
import sys

import biotite.sequence.io.fasta as fasta
import biotite.sequence.align as align
import biotite.sequence as sequence

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
    matrix_dict = align.SubstitutionMatrix.dict_from_str(matrix_str)
    matrix = align.SubstitutionMatrix(pb_alphabet, pb_alphabet, matrix_dict)
    return matrix


matrix_substitution = create_matrix()
##################################################################################

# utility constants
LENGTH_HEADER = 25
BREAK_LENGTH = 50


# function for parsing protein blocks from FASTA files
def read_sequences_from_fasta(paths):
    names = []
    sequences = []

    for path in paths:
        fasta_file = fasta.FastaFile.read(path)
        for name, sequence in fasta_file.items():
            names.append(name)
            sequence = load_pb_data.transform_seq_line(sequence)


            # print(sequence)

            if 'Z' in sequence:
                print(name + ": Unvalid PB sequence.", file= sys.stderr)
                return None

            sequences.append(sequence)

    return [names, sequences]


# function for generating textual report for alignment of two PB sequences
def generate_pairwise_alignment_report(aligns, output_file = True):
    lines = []
    lines.append("*****************")
    print("*****************")

    for a in aligns:
        n = len(a)
        lines.append(("Duzina poravnanja: " + str(n)))
        print("Duzina poravnanja: " + str(n))

        codes = align.get_codes(a)

        number_of_matched = 0
        matched_positions = []
        number_of_insertions = 0
        number_of_deletions = 0

        for i in range(n):
            if codes[0][i] == codes[1][i] and codes[0][i] != -1:
                number_of_matched += 1
                matched_positions.append(True)

            else:
                matched_positions.append(False)

            if codes[0][i] == -1:
                number_of_insertions += 1

            if codes[1][i] == -1:
                number_of_deletions += 1

        lines.append(("Broj poklopljenih: " + str(number_of_matched)))
        print("Broj poklopljenih: " + str(number_of_matched))
        lines.append(("Broj insercija: " + str(number_of_insertions)))
        print("Broj insercija: " + str(number_of_insertions))
        lines.append(("Broj delecija: " + str(number_of_deletions)))
        print("Broj delecija: " + str(number_of_deletions))
        lines.append(("Mera identity: " + str(align.get_sequence_identity(a))))
        print("Mera identity: " + str(align.get_sequence_identity(a)))
        lines.append(("Score poravnanja: " + str(align.score(a, matrix_substitution))))
        print("Score poravnanja: " + str(align.score(a, matrix_substitution)))
        lines.append("")
        print()

        symbols = align.get_symbols(a)

        for i in range(0, n, BREAK_LENGTH): # TODO: Odvoji u zasebnu funkciju
            m = i + BREAK_LENGTH
            if m > n:
                m = n

            lines.append((str(i) + " "*(BREAK_LENGTH-2) + str(m-1)))
            print(str(i) + " "*(BREAK_LENGTH-2) + str(m-1))

            line = ''
            for j in range(i, m):
                s = symbols[0][j]
                if s is None:
                    line += '-'
                    print('-', end='')
                else:
                    line += s
                    print(s, end='')

            lines.append(line)
            print()

            line = ''
            for j in range(i, m):
                if matched_positions[j]:
                   line += '|'
                   print('|' , end = '')
                else:
                   line += ' '
                   print(' ', end = '')

            lines.append(line)
            print()

            line = ''
            for j in range(i, m):
                s = symbols[1][j]
                if s is None:
                    line += '-'
                    print('-', end='')
                else:
                    line += s
                    print(s, end='')

            lines.append(line)
            print()

        lines.append("*****************")
        print("*****************")

    return lines


# function for execution alignment of two PB sequences
def execute_alignment_of_two_pb_sequences(sequences, type_a="l"):
    sequences = [load_pb_data.transform_seq_line(s) for s in sequences]
    sequences_pb = [sequence.GeneralSequence(pb_alphabet, sequence = s)
                    for s in sequences]

    aligns = None

    if type_a == "l":
        aligns = align.align_optimal(sequences_pb[0], sequences_pb[1], matrix=matrix_substitution, local=True)
        aligns = aligns[0]
    else:
        aligns = align.align_optimal(sequences_pb[0], sequences_pb[1], matrix=matrix_substitution, local=False)
        aligns = aligns[0]

    return [aligns]


# wrapper function for execution alignment and generating textual report
def execute_alignment_and_generate_report(paths, type_a='l', matrix = matrix_substitution):
    sequences_with_metadata = read_sequences_from_fasta(paths)

    if sequences_with_metadata is None:
        return None

    sequences = sequences_with_metadata[1]
    labels = sequences_with_metadata[0]
    aligns = None
    lines = []

    if type_a == 'l':
        aligns = execute_alignment_of_two_pb_sequences(sequences, type_a="l")
        lines.append("Izvestaj lokalnog poravnanja izmedju dve PB sekvence:")
        print("Izvestaj lokalnog poravnanja izmedju dve PBsekvence:")
        lines += generate_pairwise_alignment_report(aligns)

    else:
        aligns = execute_alignment_of_two_pb_sequences(sequences, type_a="g")
        lines.append("Izvestaj globalnog poravnanja izmedju dve PB sekvence:")
        print("Izvestaj globalnog poravnanja izmedju dve PB sekvence:")
        lines += generate_pairwise_alignment_report(aligns)

    return [labels, aligns, lines]


# wrapper function for loading sequences from PDB database,
# execution their alignment and generating report of this alignment
def load_pbs_and_execute_pairwise_alignment_with_report(pdbs, type_a = "l"):
    paths = []
    for pdb in pdbs:
        load_pb_data.load_pb_format(pdb)
        paths.append(pdb + ".PB.fasta")
    alignment_results = execute_alignment_and_generate_report(paths, type_a)
    return alignment_results
