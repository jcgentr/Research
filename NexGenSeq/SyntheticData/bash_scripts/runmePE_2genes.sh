#!/bin/bash
echo "This is a shell script"
counter=0
for ((n=0;n<1;n++)); do
counter=$((counter+1));
echo "Counter: $counter time(s)";
rm -rf trinity_out_dir;
rm right_reads1.fa;
rm left_reads1.fa;
rm right_reads2.fa;
rm left_reads2.fa;
rm Gene1.fa;
rm Gene2.fa;
rm Trinity.fasta;
rm Trinity.timing;
python PE_reads_FR_2genes.py;
$TRINITY_HOME/Trinity --seqType fa --left left_reads1.fa,left_reads2.fa --right right_reads1.fa,right_reads2.fa --SS_lib_type FR --CPU 8 --max_memory 20G;
mv trinity_out_dir/Trinity.fasta Trinity.fasta;
mv trinity_out_dir/Trinity.timing Trinity.timing;
# python comparegenes.py;
echo "End of script";
done

