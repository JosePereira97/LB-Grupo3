from Bio import Entrez
from Bio import SeqIO



print('A criar ficheiro...')
Output = 'PRSS1homologos3.fasta'
ficheiro_output = open(Output, 'w+')
ficheiro = open('id_listDNA(PRSS1).txt', 'r')
b_file = ficheiro.readlines()
print('A recolher informações...')
for a in b_file:
    Entrez.email = 'example@gmail.com'
    File = Entrez.efetch(db= 'nucleotide', id= a, retmode='text', rettype= 'fasta')
    print(File)
    read = SeqIO.read(File, 'fasta')
    File.close()
    ficheiro_output.write('>' + a + str(read.seq) + '\n' + '\n')
print('Ficheiro gravado sobre o nome ' + Output)
