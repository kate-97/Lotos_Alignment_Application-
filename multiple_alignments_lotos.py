# Implementations of functions for loading AA sequences, their multiple alignment and generating textual report

# necessary imports
import biotite
import biotite.sequence as sequence
import biotite.sequence.align as alignment
import biotite.sequence.graphics as graphics
from biotite.sequence.io import fasta
from matplotlib import pyplot as plt
import seaborn


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

# function for reading AA sequences from FASTA files
def read_sequences_from_fasta(paths):
    names = []
    sequences = []

    for path in paths:
        fasta_file = fasta.FastaFile.read(path)
        for name, sequence in fasta_file.items():
            names.append(name)
            sequences.append(sequence)

    return [names, sequences]


# function for generating textual report of multiple AA alignment
def generate_multi_alignment_report(align, annotated_sequences, distance_matrix, tree, output_file=True):
    lines = []
    lines.append("*****************")
    labels_formated = [decrease_name_size(l) for l in annotated_sequences[0]]
    m = len(align[0])
    n = len(align)
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

    line = 'Alignment score: ' + str(alignment.score(align, matrix = alignment.SubstitutionMatrix.std_protein_matrix()))
    lines.append(line)
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


# function for executing multiple AA alignment and generating textual report of this alignment
def execute_alignment_and_generate_report(paths):
    annotated_sequences = read_sequences_from_fasta(paths)
    labels = annotated_sequences[0]
    protein_sequences = [sequence.ProteinSequence(s) for s in annotated_sequences[1]]
    align, order, tree, distance_matrix = alignment.align_multiple(protein_sequences,
                                                                   biotite.sequence.align.SubstitutionMatrix.std_protein_matrix())
    alignment_data = {}
    alignment_data['alignment'] = align
    alignment_data['order'] = order
    alignment_data['tree'] = tree
    alignment_data['distance_matrix'] = distance_matrix
    lines = generate_multi_alignment_report(align, annotated_sequences, distance_matrix, tree)
    return labels, alignment_data, lines

