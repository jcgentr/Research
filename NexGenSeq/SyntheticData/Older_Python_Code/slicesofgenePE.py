# -*- coding: utf-8 -*-
"""
Spyder Editor

nexgen sequencing
making slices of a gene
These are SINGLE END reads.

Author: Jared Gentry
Date: December 15, 2017 18:16

"""
import random

# need bases for gene construction
bases = ['A', 'G', 'C', 'T']

# main variables to change
gene_length = random.randint(2000,3000)
#gene_length = 2000
slice_length = 100
#slices_per_copy = random.randint(2000,9000)
slices_per_copy = 5500
no_of_copies = 100

gene = []
for x in range(gene_length):
    addBase = random.randint(0,3)
    gene.append(bases[addBase])
    
# additional variables
slices = []
segment_no = []
totalSegments = slices_per_copy * no_of_copies

for s in range(totalSegments):
    segment_no.append("segment" + str(s + 1))

for j in range(slices_per_copy):
    #randomint has inclusive range
    startIndex = random.randint(0,(gene_length - slice_length))
    slices.append(gene[startIndex:(startIndex + slice_length)])

reverse_reads = []
for k in range(len(slices)):
        fragment=slices[k]
        for j in range(len(fragment)):
            if fragment[j] == 'A':
                fragment[j] = 'T'
            elif fragment[j] == 'T':
                fragment[j] = 'A'
            elif fragment[j] == 'C':
                fragment[j] = 'G'
            elif fragment[j] == 'G':
                fragment[j] = 'C'
                
        fragment_str = ''.join(fragment)
        reverse_reads.append(fragment_str[::-1])

for i in range(slices_per_copy):
    for c in range(no_of_copies - 1):
            slices.append(slices[i])
            reverse_reads.append(reverse_reads[i])
        
print("\n") 

a = len(slices[0])
print(a)
b = len(slices)
print(b)

# write the number of reads to results.txt file
#f = open('results.txt','a')
#f.write('\n' + str(totalSegments))
#f.close()

# write slices to a FASTA file for Trinity
ofile = open("left_reads.fa", "w")
count = 0
for i in range(len(slices)):
    seq = ''.join(slices[i])
    ofile.write(">" + segment_no[i] + "/1" + "\n" + seq + "\n")
    count = count + 1

#do not forget to close it
print(count)
ofile.close()

ofile = open("right_reads.fa", "w")
count = 0
for i in range(len(reverse_reads)):
    ofile.write(">" + segment_no[i] + "/2" + "\n" + reverse_reads[i] + "\n")
    count = count + 1

#do not forget to close it
print(count)
ofile.close()


# write gene to a FASTA file for comparison with Trinity's output
ofile = open("Gene.fa", "w")
countg = 0
ofile.write(">gene"+str(len(gene)))
for i in range(len(gene)):
    if countg % 60 == 0:
        ofile.write("\n")
    ofile.write(gene[i])
    countg = countg + 1

#do not forget to close it
print(countg)
ofile.close()