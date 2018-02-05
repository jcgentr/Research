# -*- coding: utf-8 -*-
"""
Spyder Editor

nexgen sequencing
making slices of multiple genes

Author: Jared Gentry
Date: January 23, 2018 11:55

"""
import random

# 4 possible bases for gene
bases = ['A', 'G', 'C', 'T']

# variables to modify
#gene_length = random.randint(2000,20000)
gene_length = 2000
slice_length = 100
#slices_per_copy = random.randint(2000,9000)
slices_per_copy = 5000
no_of_copies = 100

# generate random genes
gene = []
for x in range(gene_length):
    addBase = random.randint(0,3)
    gene.append(bases[addBase])
    
gene2 = []
for x in range(gene_length):
    addBase = random.randint(0,3)
    gene2.append(bases[addBase])
    
# variables
slices = []

segment_no = []
totalSegments = slices_per_copy * no_of_copies

for s in range(totalSegments):
    segment_no.append("segment" + str(s + 1))

for j in range(slices_per_copy):
    #randomint has inclusive range
    startIndex = random.randint(0,(gene_length - slice_length))
    slices.append(gene[startIndex:(startIndex + slice_length)])

for i in range(slices_per_copy):
    for c in range(no_of_copies - 1):
            slices.append(slices[i])
            
for s in range(totalSegments):
    segment_no.append("segment" + str(s + 1))

slices2 = []
for j in range(slices_per_copy):
    #randomint has inclusive range
    startIndex = random.randint(0,(gene_length - slice_length))
    slices2.append(gene2[startIndex:(startIndex + slice_length)])

for i in range(slices_per_copy):
    for c in range(no_of_copies - 1):
            slices2.append(slices2[i])
        
print("\n") 

a = len(slices[0])
print(a)
b = len(slices)
print(b)
c = len(slices2)
print(c)

# file-append
#f = open('results.txt','a')
#f.write('\n' + str(totalSegments))
#f.close()

# write slices to a FASTA file for Trinity
ofile = open("gene_slices1.fa", "w")

for i in range(len(slices)):
    seq = ''.join(slices[i])
    ofile.write(">" + segment_no[i] + "\n" + seq + "\n")

#do not forget to close it
ofile.close()

# write slices to a FASTA file for Trinity
ofile = open("gene_slices2.fa", "w")

for i in range(len(slices2)):
    seq = ''.join(slices2[i])
    ofile.write(">" + segment_no[i] + "\n" + seq + "\n")

#do not forget to close it
ofile.close()


# write gene to a FASTA file
ofile = open("Gene1.fa", "w")
countg = 0
ofile.write(">gene")
for i in range(len(gene)):
    if countg % 60 == 0:
        ofile.write("\n")
    ofile.write(gene[i])
    countg = countg + 1

#do not forget to close it
print(countg)
ofile.close()

# write gene to a FASTA file
ofile = open("Gene2.fa", "w")
countg = 0
ofile.write(">gene")
for i in range(len(gene2)):
    if countg % 60 == 0:
        ofile.write("\n")
    ofile.write(gene2[i])
    countg = countg + 1

#do not forget to close it
print(countg)
ofile.close()
