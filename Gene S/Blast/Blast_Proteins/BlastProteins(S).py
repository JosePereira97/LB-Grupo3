from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio import ExPASy

def get_prot(id):
    
    with ExPASy.get_sprot_raw(id) as handle:
        seq_record = SeqIO.read(handle, "swiss")
    tam= len(seq_record.seq)
    seq = seq_record.seq
    tax= seq_record.annotations["taxonomy"]
    org= seq_record.annotations["organism"]
    #host= seq_record.annotations["organism_host"]
    y = ('ID:' + id + '|' + 'SEQUENCE:' + seq + '|' + 'SEQUENCE LENGTH:' + str(tam) + 'bp' + '|' + 'TAXONOMY:' + str(tax) + '|' + 'ORGANISM:' + org )
    return y


idS = 'P0DTC2' #ID na swissprot do S
x = get_prot(idS)
result_handle = NCBIWWW.qblast('blastp', 'nr', x)
with open('blastProtein(S)', "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()