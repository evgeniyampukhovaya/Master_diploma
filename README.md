# Master_diploma
Code for ChIP-seq peak intersections and motif finding
#Intersections of 2 bed files (genome intervals)

Intersection_bed_files.py - find overlapping regions in 2 bed files
Sample files: bed_file1.bed, bed_file2.bed, bed_file_result.bed

#Find motifs using PWMs

PFM_to_PWM.py - converts frequency matrix into position weight matrix
find_motifs_in_fasta.py - find motif coordinates using PWM
find_motifs_in_fasta_optimized.py - the same as find_motifs_in_fasta.py, but works faster
Sample files: PFM.txt, PWM.txt, fasta_file_for_motif_search.fasta, motif_coordinates_results.txt

#De novo motif search
Homer.txt - commands for Homer tool using genome and random background (for more information, read Homer manual)

#Make a list of promoter coordinates (-1500; +longest UTR) from gff genome annotation

#Intersections of peaks with promoters

#Make fasta from bed
