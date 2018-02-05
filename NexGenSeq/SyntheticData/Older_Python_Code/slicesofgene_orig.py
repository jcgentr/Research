#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:02:08 2018

@author: jcgantr

Spyder Editor

nexgen sequencing
making slices of a gene

Author: Jared Gentry

"""
import random

# need random 2000 bp gene
bases = ['A', 'G', 'C', 'T']

#gene_length = int(input("What is the length of the gene? \n"))
#slice_length = int(input("How long (bp's) is each segment to slice? \n"))
#slices_per_copy = int(input("How many segments do you want? \n"))
#gene_length = random.randint(2000,20000)

gene_length = 2000
slice_length = 200
slices_per_copy = 100
no_of_copies = 20000

gene = []
for x in range(gene_length):
    addBase = random.randint(0,3)
    gene.append(bases[addBase])
    
# variables
slices = []

segment_no = []
for s in range(slices_per_copy):
    segment_no.append("segment" + str(s + 1))

for i in range(no_of_copies):
    for j in range(int(slices_per_copy)):
        #randomint has inclusive range
        startIndex = random.randint(0,(gene_length - slice_length))
        slices.append(gene[startIndex:(startIndex + slice_length)])
        
print("\n") 

a = len(slices[0])
print(a)
b = len(slices)
print(b)

# write slices to a FASTA file for Trinity
ofile = open("gene_slices.fa", "w")
count = 0
for i in range(len(slices)):
    seq = ''.join(slices[i])
    ofile.write(">" + segment_no[i] + "\n" + seq + "\n")
    count = count + 1

#do not forget to close it
print(count)
ofile.close()


# write gene to a FASTA file for Trinity
ofile = open("Gene.fa", "w")
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