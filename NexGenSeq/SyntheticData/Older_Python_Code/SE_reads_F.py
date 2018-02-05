# -*- coding: utf-8 -*-
"""
Spyder Editor

Next-Generation Sequencing (NGS)
Makes fragments of gene and SE reads of those fragments
Outputs 1 FASTA file of the forward reads
Forward reads == sense strand 5' to 3' direction

Author: Jared Gentry
Date Created: January 26, 2018 11:30 AM

"""
import random

# function definitions
def make_a_gene(gene_length):
    """
        INPUT: length of gene you want to create
        OUTPUT: gene as a list of bases
    """
    # need bases for gene construction
    bases = ['A', 'G', 'C', 'T']
    gene = []
    for x in range(gene_length):
        addBase = random.randint(0,3)
        gene.append(bases[addBase])  
    return gene

def make_fragments(gene,fragment_length,total_fragments):
    """
    """
    fragments = []
        
    for i in range(total_fragments):
        # randomint has inclusive range
        startIndex = random.randint(0,(len(gene) - fragment_length))
        # fragments is a list of lists from gene
        fragments.append(gene[startIndex:(startIndex + fragment_length)])

    return fragments

def make_reads(fragments,read_length,total_reads):
    """
    """
    reads = []
    for i in range(total_reads):
        fragment_index = random.randint(0,(len(fragments)-1))
        fragment = ''.join(fragments[fragment_index])
        reads.append(fragment[0:read_length])
    return reads
      
def output_reads(reads,ofile):
    """
    """
    count = 0
    for i in range(len(reads)):
        read_number = "read" + str(i + 1)
        ofile.write(">" + read_number + "\n" + reads[i] + "\n")
        count = count + 1
    
    #do not forget to close it
    print("Number of reads: " + str(count))
    ofile.close()
    
def output_gene(gene,ofile):
    """
    """
    count = 0
    ofile.write(">gene")
    for i in range(len(gene)):
        if count % 60 == 0:
            ofile.write("\n")
        ofile.write(gene[i])
        count = count + 1
    
    #do not forget to close it
    print("Length of gene: " + str(count))
    ofile.close()
    
"""
    THIS IS THE BODY OF THE PROGRAM
"""
# main variables to change
gene_length = random.randint(2000,3000)
fragment_length = 500
total_fragments = 10000
read_length = 76
total_reads = 1000000

# generate a gene
gene = make_a_gene(gene_length)

# make fragments of that gene
fragments = make_fragments(gene,fragment_length,total_fragments)

# make reads of fragments
reads = make_reads(fragments,read_length,total_reads)

# write slices to a FASTA file for Trinity
ofile = open("gene_slices.fa", "w")
output_reads(reads,ofile)

# write gene to a FASTA file for comparison with Trinity's output
ofile = open("Gene.fa", "w")
output_gene(gene,ofile)

# write the number of reads to results.txt file
#f = open('results.txt','a')
#f.write('\n' + str(totalSegments))
#f.close()
