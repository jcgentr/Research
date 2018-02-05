#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:14:28 2018

@author: jcgantr
"""
def read_fasta(fp):
        name, seq = None, []
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq))
                name, seq = line, []
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))

with open('Gene.fa') as fp:
    for name, seq1 in read_fasta(fp):
        Python_gene = seq1

#print(Python_gene)
PythonGene_length = len(Python_gene)

with open('Trinity.fasta') as fp:
    for name, seq2 in read_fasta(fp):
        Trinity_gene = seq2

#print(Trinity_gene)
TrinityGene_length = len(Trinity_gene)

result = Trinity_gene in Python_gene

print(result)

# file-append.py
f = open('results.txt','a')
f.write('\n' + str(PythonGene_length) + " " + str(TrinityGene_length) + " " + str(result))
f.close()