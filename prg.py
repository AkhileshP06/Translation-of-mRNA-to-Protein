import random

Dseq = ""
Nuc = ["A","C","T","G"]
for i in range(0,15):
    Dseq = Dseq+Nuc[random.randrange(0,4)]
print("DNA sequence is : ",Dseq)
print()
Rseq = Dseq.replace("T","U")
print("RNA sequence is : ",Rseq)

print("length of mRNA sequence : ",len(Rseq))
print()
if(len(Rseq)%3!=0):
    print("Nucleotide sequence does not have whole number of codons")
    print("remove ",len(Rseq)%3," nucleotides to get accurate results")
def translate(Rseq):
    table={'AUA':'Ile', 'AUC':'Ile', 'AUU':'Ile', 'AUG':'Met',
           'ACA':'Thr', 'ACC':'Thr', 'ACG':'Thr', 'ACU':'Thr',
           'AAC':'Asn', 'AAU':'Asn', 'AAA':'Lys', 'AAG':'Lys',
           'AGC':'Ser', 'AGU':'Ser', 'AGA':'Arg', 'AGG':'Arg',                 
           'CUA':'Leu', 'CUC':'Leu', 'CUG':'Leu', 'CUU':'Leu',
           'CCA':'Pro', 'CCC':'Pro', 'CCG':'Pro', 'CCU':'Pro',
           'CAC':'His', 'CAU':'His', 'CAA':'Gln', 'CAG':'Gln',
           'CGA':'Arg', 'CGC':'Arg', 'CGG':'Arg', 'CGU':'Arg',
           'GUA':'Val', 'GUC':'Val', 'GUG':'Val', 'GUU':'Val',
           'GCA':'Ala', 'GCC':'Ala', 'GCG':'Ala', 'GCU':'Ala',
           'GAC':'Asp', 'GAU':'Asp', 'GAA':'Glu', 'GAG':'Glu',
           'GGA':'Gly', 'GGC':'Gly', 'GGG':'Gly', 'GGU':'Gly',
           'UCA':'Ser', 'UCC':'Ser', 'UCG':'Ser', 'UCU':'Ser',
           'UUC':'Phe', 'UUU':'Phe', 'UUA':'Leu', 'UUG':'Leu',
           'UAC':'Tyr', 'UAU':'Tyr', 'UAA':'_', 'UAG':'_',
           'UGC':'Cys', 'UGU':'Cys', 'UGA':'_', 'UGG':'Trp',}
    protein=""
    if len(Rseq)%3 == 0:
        for i in range(0,len(Rseq),3):
            codon=Rseq[i:i+3]
            protein+=table[codon]+"-"
    return protein
p=translate(Rseq[0:len(Rseq)])
print("Number of codons translated : ",int(len(Rseq)/3))
print()
print("Protein sequence is",p)
