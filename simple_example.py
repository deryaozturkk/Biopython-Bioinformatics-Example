from Bio.SeqIO import parse
from Bio.Seq import Seq
from Bio.Data import IUPACData


print("....................Bioinformatics File And Content....................")
file=open("example.fasta")
records=parse(file,"fasta")
for record in records:
    #print(record)
    print("ID: %s" % (record.id))
    print("Name: %s" % record.name)
    print("Description: %s" % (record.description))
    print("Annotations: %s" % (record.annotations))
    print("Sequence Data: %s" % (record.seq))
    

#Sequence
print(".......Sequence.......")
seq1=Seq("AGCT")
print(seq1) #output => AGCT

#Alphabet Module
#Biopython version 1.77'den sonra Alphabet modülü kaldırılmıştır.
#Seq("ACGT",Bio.Alphabet) kullanımı yerine Seq("ACGT") kullanılacaktır
print(".......IUPAC Data.......")
print(IUPACData.protein_letters) #output => ACDEFGHIKLMNPQRSTVWY


#Basic Operarions
print(".......Basic Operations........")
seq_string=Seq("AGCTAGCT")
print("to get the first value seq[0] => ", seq_string[0]) #output => 0. indis A
print("to get the first two values seq[0:2] => ", seq_string[0:2]) #0. indisten 2.indise kadar alır
print("to get all values seq[:] => ", seq_string[:]) #tüm stringi alır
print("to get length len(seq_string) => ", len(seq_string))
print("to get count of a value seq_string.count('A') => ", seq_string.count('A'))

#add two sequence
seq1=Seq("AGCT")
#seq2=Seq("TCGA",generic_dna) bu kullanım 1.81'de kaldırılmıştır
seq2=Seq("TCGA")
print("add two sequence seq1+seq2 => ", seq1+seq2)

#add different type protein
seq3=Seq("AGCTACATTAGC")
seq4=Seq("AGCUACGUGAUA")
print("add two sequence seq1+seq2 => ", seq3+seq4)
#biopython 1.81 protein ve dna toplanmasını kontrol etmiyor
#bu kontrolü kullanıcı yapmalı
#adding many sequences
print("Add two or more sequences [Seq('AGCT'),Seq('CTAT')] => ")
list=[Seq("AGCT"),Seq("CTAT"),Seq("TGCA"),Seq("CAGT")]
for i in list:
    print(i)

final_seq=Seq("")
for i in list:
    final_seq+=i
print(final_seq)

#change  case of sequence
rna=Seq("agctagtat")
print("case sensitivity => ",'A' in rna)
print("case sensitivity => ",'a' in rna)
print("case sensitivity => ",'GCT' in rna)
print("change  case of sequence rna.upper() => ", rna.upper())

#to find letter in sequence
protein_seq=Seq("AGCUAGCAUGCGAU")
print("to find letter in sequence seq.find('A') => " , protein_seq.find('A')) #ilk olarak A nükleotidini bulduğu indis
print("to find letter in sequence seq.find('AG') => " ,protein_seq.find('AG'))
print("to find letter in sequence seq.find('AU') => " ,protein_seq.find('AU'))


#split operation
protein_seq1=Seq("AGUACACUGGU")
print("to perform splitting operation seq.split('A') => " , protein_seq1.split('A'))

#strip operations in sequence
protein_seq2=Seq("     AGCT     ")
print("to perform strip operations in the sequence seq.strip() => " , protein_seq2.strip())

