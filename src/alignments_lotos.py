# Implementations of functions for loading AA sequences, their pairwise alignment and generating textual report

# necessary imports
import biotite.sequence.io.fasta as fasta
import biotite.sequence.align as align
import biotite.sequence as sequence


# utility function for name compress
def decrease_name_size(name):
    lind = name.find('|')
    s = name[lind+1:]
    rind = s.find('|')

    if rind == '-1':
        rind = s.find(' ')

    return s[:rind]


# utility constants
LENGTH_HEADER = 25
BREAK_LENGTH = 50


# function for reading AA sequences from FASTA files
def read_sequences_from_fasta(paths):
    names = []
    sequences = []

    for path in paths:
        fasta_file = fasta.FastaFile.read(path)

        if len(list(fasta_file.items())) == 0:
            return None

        for name, sequence in [list(fasta_file.items())[0]]:
            names.append(decrease_name_size(name))
            sequences.append(sequence)

    return [names, sequences]


# function for generating textual report for alignment of two AA sequences
def generate_pairwise_alignment_report(aligns, output_file = True, open_penalty=-10, continue_penalty=0):
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

        lines.append(("Broj poklopljenih aminokiselina: " + str(n)))
        print("Broj poklopljenih aminokiselina: " + str(n))
        lines.append(("Broj insercija: " + str(number_of_insertions)))
        print("Broj insercija: " + str(number_of_insertions))
        lines.append(("Broj delecija: " + str(number_of_deletions)))
        print("Broj delecija: " + str(number_of_deletions))
        lines.append(("Kazna za otvaranje praznina: " + str(open_penalty)))
        print(("Kazna za otvaranje praznina: " + str(open_penalty)))
        lines.append(("Kazna za produzavanje praznina: " + str(continue_penalty)))
        print(("Kazna za produzavanje praznina: " + str(continue_penalty)))
        lines.append(("Mera identity: " + str(align.get_sequence_identity(a))))
        print("Mera identity: " + str(align.get_sequence_identity(a)))
        lines.append("")
        lines.append(("Skor: " + str(align.score(a, align.SubstitutionMatrix.std_protein_matrix()))))
        print("Skor: " + str(align.score(a, align.SubstitutionMatrix.std_protein_matrix())))
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


# function which calls appropriate function for alignment of two AA sequences
def execute_alignment_of_two_aa_sequences(sequences, type_a="l", matrix=align.SubstitutionMatrix.std_protein_matrix(), open_penalty=-10, continue_penalty=0):
    seq1 = sequence.ProteinSequence(sequences[0])
    seq2 = sequence.ProteinSequence(sequences[1])
    aligns = None

    if type_a == "l":
        aligns = align.align_optimal(seq1, seq2, matrix=matrix, local=True, gap_penalty = (open_penalty, continue_penalty))
        aligns = aligns[0]
    else:
        aligns = align.align_optimal(seq1, seq2, matrix=matrix, local=False, gap_penalty = (open_penalty, continue_penalty))
        aligns = aligns[0]
    return [aligns]

# wrapper function in which is called function for execution alignment and function for generating textual reports
def execute_alignment_and_generate_report(paths, type_a='l', matrix = align.SubstitutionMatrix.std_protein_matrix(), open_penalty=-10, continue_penalty=0):
    sequences_with_metadata = read_sequences_from_fasta(paths)
    sequences = sequences_with_metadata[1]
    labels = sequences_with_metadata[0]
    aligns = None
    lines = []

    if type_a == 'l':
        aligns = execute_alignment_of_two_aa_sequences(sequences, type_a="l", matrix = matrix, open_penalty = open_penalty, continue_penalty = continue_penalty)
        lines.append("Izvestaj lokalnog poravnanja izmedju dve proteinske sekvence " + labels[0] + " i " + labels[1])
        print("Izvestaj lokalnog poravnanja izmedju dve proteinske sekvence:" +  labels[0] + " i " + labels[1])
        lines += generate_pairwise_alignment_report(aligns)

    else:
        aligns = execute_alignment_of_two_aa_sequences(sequences, type_a="g", matrix = matrix,  open_penalty=-10, continue_penalty=0)
        lines.append("Izvestaj globalnog poravnanja izmedju dve proteinske sekvence:" + labels[0] + " i " + labels[1])
        print("Izvestaj globalnog poravnanja izmedju dve proteinske sekvence:" + labels[0] + " i " + labels[1])
        lines += generate_pairwise_alignment_report(aligns, open_penalty=open_penalty, continue_penalty=continue_penalty)

    return [labels, aligns, lines]