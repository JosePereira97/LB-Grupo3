from Bio import Entrez
from Bio import SeqIO

print('A criar ficheiro...')
Output = 'SHomologosDNA.fasta'
ficheiro_output = open(Output, 'w+')
ficheiro = open('id_listDNA(S).txt', 'r')
b_file = ficheiro.readlines()
print('A recolher informações...')
for a in b_file:
    Entrez.email = 'example@gmail.com'
    File = Entrez.efetch(db= 'Nucleotide', id= a, retmode='text', rettype= 'fasta')
    print(File)
    read = SeqIO.read(File, 'fasta')
    File.close()
    ficheiro_output.write('>' + a + str(read.seq) + '\n' + '\n')
print('Ficheiro gravado sobre o nome ' + Output)