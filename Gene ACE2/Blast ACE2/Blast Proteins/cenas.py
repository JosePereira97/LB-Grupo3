from Bio import Entrez
from Bio import SeqIO

print('A criar ficheiro...')
Output = 'ACE2homologos3.fasta'
ficheiro_output = open(Output, 'w+')
ficheiro = open('id_list_prot(ACE2).txt', 'r')
b_file = ficheiro.readlines()
print('A recolher informações...')
for a in b_file:
    Entrez.email = 'example@gmail.com'
    File = Entrez.efetch(db= 'Protein', id= a, retmode='text', rettype= 'fasta')
    print(File)
    read = SeqIO.read(File, 'fasta')
    File.close()
    ficheiro_output.write('>' + a + str(read.seq) + '\n' + '\n')
print('Ficheiro gravado sobre o nome ' + Output)