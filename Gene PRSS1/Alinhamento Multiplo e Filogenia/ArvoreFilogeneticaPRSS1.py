from Bio import Phylo

arvore1 = Phylo.read('ÁrvoreFilogenéticaPRSS1.dnd','newick')
print(arvore1)

Phylo.draw_ascii(arvore1)