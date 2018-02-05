#!/bin/bash
echo "This is a shell script"
counter=0
for ((n=0;n<20;n++)); do
counter=$((counter+1));
echo "Counter: $counter time(s)";
rm -rf trinity_out_dir;
rm gene_slices.fa;
rm Gene.fa;
rm Trinity.fasta;
rm Trinity.timing;
# python SE_reads_F.py;
python slicesofgene.py
$TRINITY_HOME/Trinity --seqType fa --single gene_slices.fa --SS_lib_type F --CPU 8 --max_memory 20G;
mv trinity_out_dir/Trinity.fasta Trinity.fasta;
mv trinity_out_dir/Trinity.timing Trinity.timing;
python comparegenes.py;
echo "End of script";
done