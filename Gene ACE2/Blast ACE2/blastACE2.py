result_handle = open("ACE2blast.xml")

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)

E_VALUE_THRESH = 0.04

for alignment in blast_record.alignments:
     for hsp in alignment.hsps:
         if hsp.expect < E_VALUE_THRESH:
             print("****Alignment****")
             print("sequence:", alignment.title)
             print("length:", alignment.length)
             print("e value:", hsp.expect)
             print(hsp.query[0:75] + "...")
             print(hsp.match[0:75] + "...")
             print(hsp.sbjct[0:75] + "...")

from Bio import SearchIO
blast_qresult = SearchIO.read("ACE2blast.xml", "blast-xml")
print(blast_qresult)
blast_hit = blast_qresult[0]    # first hit from the query result('que é o nosso gene')
print(blast_hit)
for i in range(1,5):
    print(blast_qresult[i])