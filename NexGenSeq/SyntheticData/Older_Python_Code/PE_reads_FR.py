# -*- coding: utf-8 -*-
"""
Spyder Editor

Next-Generation Sequencing (NGS)
Makes fragments of gene and PE reads of those fragments
Outputs 2 FASTA files of the forward (left) and reverse (right) reads
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
    rev_reads = []
    rev_frag = []
    for i in range(total_reads):
        fragment_index = random.randint(0,(len(fragments)-1))
        fragment = ''.join(fragments[fragment_index])
        rev_frag = fragments[fragment_index]
        reads.append(fragment[0:read_length])
        for j in range(len(rev_frag)):
            if rev_frag[j] == 'A':
                rev_frag[j] = 'T'
            elif rev_frag[j] == 'T':
                rev_frag[j] = 'A'
            elif rev_frag[j] == 'C':
                rev_frag[j] = 'G'
            elif rev_frag[j] == 'G':
                rev_frag[j] = 'C'
        rev_fragment = ''.join(rev_frag)
        rev_fragment = rev_fragment[::-1]
        rev_reads.append(rev_fragment[0:read_length])
    return [reads,rev_reads]

def make_reverse_gene(gene):
    """
    """
    rev_gene = []
    for i in range(len(gene)):
        rev = gene[i]
        if rev == 'A':
            rev = 'T'
        elif rev == 'T':
            rev = 'A'
        elif rev == 'C':
            rev = 'G'
        elif rev == 'G':
            rev = 'C'
        rev_gene.append(rev)
    return rev_gene
      
def output_reads(reads,ofile,left_or_right):
    """
    """
    count = 0
    for i in range(len(reads)):
        read_number = "read" + str(i + 1) + "/" + str(left_or_right)
        ofile.write(">" + read_number + "\n" + reads[i] + "\n")
        count = count + 1
    
    #do not forget to close it
    print("Number of reads: " + str(count))
    ofile.close()
    
def output_gene(gene,ofile,sense_or_antisense):
    """
    """
    count = 0
    if sense_or_antisense == "antisense":
        ofile.write("\n")
    ofile.write(">" + sense_or_antisense + str(len(gene)))
    for i in range(len(gene)):
        if count % 60 == 0:
            ofile.write("\n")
        ofile.write(gene[i])
        count = count + 1
    
    #do not forget to close it
    print("Length of gene: " + str(count))
    
"""
    THIS IS THE BODY OF THE PROGRAM
"""
# main variables to change
gene_length = random.randint(3000,9000)
fragment_length = 200
total_fragments = 10000
read_length = 100
total_reads = 500000

# generate a gene
gene = make_a_gene(gene_length)
rev_gene = make_reverse_gene(gene)

# make fragments of that gene
fragments = make_fragments(gene,fragment_length,total_fragments)

# make reads of fragments
all_reads = make_reads(fragments,read_length,total_reads)
left_reads = all_reads[0]
right_reads = all_reads[1]

# write slices to a FASTA file for Trinity
ofile = open("left_reads.fa", "w")
left = 1
output_reads(left_reads,ofile,left)
ofile = open("right_reads.fa", "w")
right = 2
output_reads(right_reads,ofile,right)

# write gene to a FASTA file for comparison with Trinity's output
ofile = open("Gene.fa", "w")
output_gene(gene,ofile,"sense")
output_gene(rev_gene,ofile,"antisense")

ofile.close()
# write the number of reads to results.txt file
#f = open('results.txt','a')
#f.write('\n' + str(totalSegments))
#f.close()
