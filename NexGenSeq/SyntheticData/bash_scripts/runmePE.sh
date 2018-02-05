#!/bin/bash
echo "This is a shell script"
counter=0
for ((n=0;n<1;n++)); do
counter=$((counter+1));
echo "Counter: $counter time(s)";
rm -rf trinity_out_dir;
rm right_reads.fa;
rm left_reads.fa;
rm Gene.fa;
rm Trinity.fasta;
rm Trinity.timing;
python PE_reads_FR.py;
#python slicesofgenePE.py
$TRINITY_HOME/Trinity --seqType fa --left left_reads.fa --right right_reads.fa --SS_lib_type FR --CPU 8 --max_memory 20G;
mv trinity_out_dir/Trinity.fasta Trinity.fasta;
mv trinity_out_dir/Trinity.timing Trinity.timing;
python comparegenes.py;
echo "End of script";
done

