# Implementations of functions for visualisations results of alignments
# All types of alignment are covered (pairwise and multiple) of both AA and PB sequences.

# necessary imports
import matplotlib.pyplot as plt
import biotite.sequence.align as align
import biotite.sequence as sequence
import biotite.sequence.align.alignment
import seaborn
from biotite.sequence import graphics
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import linkage, dendrogram


# function for similarity based visualisation of pairwise alignment
def graphical_similarity_based_alignment_visualisation(alignment, labels = None, filename='output_similarity_based.pdf', matrix = sequence.align.SubstitutionMatrix.std_protein_matrix()):
  fig = plt.figure()
  gs = fig.add_gridspec(1, 1)
  ax = fig.add_subplot(gs[0, 0])

  ax.set_title("Vizuelizacija poravnanja izmedju dve sekvence bazirana na slicnosti")
  graphics.plot_alignment_similarity_based(
  ax, alignment, matrix=matrix,
  show_numbers=True, show_line_position=True, color='cornflowerblue',
  symbols_per_line=30, labels = labels
  )
  plt.savefig(filename)


# function for classic visualisation of pairwise alignment
def graphical_classic_alignment_visualisation(alignment, labels = None, filename='output_classic.pdf'):
  fig = plt.figure(num = "Klasicna vizuelizacija poravnanja")
  gs = fig.add_gridspec(1, 1)
  ax = fig.add_subplot(gs[:, :])
  graphics.plot_alignment_type_based(
    ax, alignment,
    show_numbers=True, show_line_position=True, color_scheme='flower',
    symbols_per_line=50, labels = labels
  )


  ax.set_title("Klasicna vizuelizacija poravnanja izmedju dve sekvence")

  plt.show()

  plt.savefig(filename)


# function for classic visualisation of multiple alignment
def graphical_classic_multi_alignment_visualisation(alignment_data, labels, filename='output_classic_multi_alignment.pdf'):
  fig = plt.figure()
  gs = fig.add_gridspec(1, 1)
  ax = fig.add_subplot(gs[0, 0])
  print(alignment_data['alignment'], flush=True)
  graphics.plot_alignment_type_based(
    ax, alignment_data['alignment'], labels = labels, symbols_per_line=30,
    show_numbers=True, color_scheme="flower"
  )
  ax.set_title("Vizuelizacija visestrukog poravnanja sekvenci")
  plt.savefig(filename)


# function for visualisation of dendrogram obtained by agglomerative clustering based on obtained distances of sequences
def graphical_dendrogram_by_hierarchical_clustering(alignment_data, linkage_t ='single', file_name = 'output_dendrogeam_by_cluster_single.pdf'):
  ac = AgglomerativeClustering()
  ac.fit(alignment_data['distance_matrix'])
  linkage_matrix = linkage(alignment_data['distance_matrix'], linkage_t)
  dendrogram(linkage_matrix)
  plt.xlabel('Poravnate sekvence')
  plt.ylabel('Rastojanje')
  plt.title('Dendrogram dobijen algoritmom hijerarhijskog klasterovanja ($' + linkage_t + '$'  + '$linkage$)')
  plt.savefig(file_name)


# function for visualisation of dendrogram based on obtained distances of sequences
def graphical_dendrogram_multi_alignment_visualisation(alignment_data, labels = None, filename='output_dendrogram_multi_alignment.pdf'):
  fig = plt.figure()
  gs = fig.add_gridspec(1, 1)
  ax = fig.add_subplot(gs[0, 0])
  graphics.plot_dendrogram(ax, alignment_data['tree'], labels = labels, color='darkslateblue', orientation='top')
  ax.set_title("Drvo spajanja na osnovu matrice rastojanja")
  plt.savefig(filename)


# function for visualisation of heatmap based on obtained distances of sequences
def graphical_heatmap_multi_alignment_visualisation(alignment_data, labels = None, filename='output_heatmap_multi_alignment.pdf'):
  fig = plt.figure()
  gs = fig.add_gridspec(1, 1)
  ax = fig.add_subplot(gs[0, 0])
  ax.set_title('Matrica rastojanja izrazena toplotnom mapom')
  seaborn.heatmap(alignment_data['distance_matrix'],
                  annot=True,
                  cmap="crest",
                  xticklabels=labels,
                  yticklabels=labels)

  print(alignment_data['distance_matrix'])
  plt.savefig(filename)


'''  -- Deprecated.
def graphical_text_alignment_view(alignment, filename = 'output.pdf'):
  sequences = align.get_symbols(alignment)
  s1 = sequences[0]
  s2 = sequences[1]

  n = len(s1)
  Rows = n // 50 + 1
  Tot = Rows
  Cols = 1
  if Tot % Cols != 0:
    Rows += 1

  Position = range(1, Tot + 1)

  size = n*0.02

  if size < 5:
    size = 5
  fig = plt.figure(figsize=(10, size))

  i = 0
  for k in range(Tot):
    ax = fig.add_subplot(Rows, Cols, Position[k])
    x = 0
    ax.text(0, 1, str(i), fontsize=10)

    y1 = 0.65
    yl = 0.5
    y2 = 0.3

    for j in range(50):
      if s1[i] == '-':
        ax.text(x, y1, s1[i], fontsize=12)

      if s2[i] == '-':
        ax.text(x, y2, s2[i], fontsize=12)

      if s1[i] != '-' and s1[i] == s2[i]:
        ax.text(x, y1, s1[i], fontsize=10, color='red', fontweight='bold')
        ax.text(x, yl, '|', fontsize=8, color='red', fontweight='bold')
        ax.text(x, y2, s2[i], fontsize=10, color='red', fontweight='bold')
      else:
        if s1[i] != '-':
          ax.text(x, y1, s1[i], fontsize=8, color='blue')

        if s2[i] != '-':
          ax.text(x, y2, s2[i], fontsize=8, color='blue')

      x += 0.022
      i += 1
      if i == n:
        break

    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    ax.set_axis_off()

  plt.tight_layout()
  plt.savefig(filename)
  plt.show()
'''

''' -- Deprecated
def graphical_logo_visualisation(alignment_data, file_name = 'output_multi_alignment_logo.pdf'):
  fig = plt.figure()
  gs = fig.add_gridspec(1, 1)
  ax = fig.add_subplot(gs[0, 0])
  graphics.plot_sequence_logo(ax,
                              sequence.SequenceProfile.from_alignment(alignment_data['alignment']))
  plt.savefig(file_name)
'''