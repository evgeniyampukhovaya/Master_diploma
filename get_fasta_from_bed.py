# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:58:30 2019

@author: UbogoevaEV
"""

from Bio import SeqIO
fasta_file = 'E:/Work/Get_fasta_from_bed/TAIR10_chr_all__for_galaxy.fasta'

record_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))
with open('genes_EIN3_timeseries_12_with_input_control.bed', 'r') as bed, open ('genes_EIN3_timeseries_12_with_input_control.fasta', 'w') as file_output:
    bed_list = []
    for line in bed.readlines():
        line = line.strip()
        cols = line.split('\t')
        bed_list.append(cols)
    for i in range(len(bed_list)):
#        file_output.write(bed_list[i][0] + '>' +':' + bed_list[i][1] + '-' + bed_list[i][2] + '\t' + bed_list[i][3] + '\t' + bed_list[i][4])
#            file_output.write('>' + bed_list[i][0] + '_' + bed_list[i][4][:-1] + '_' + bed_list[i][1] + '_' + bed_list[i][2] + '_' + bed_list[i][3])
#        file_output.write('>' + bed_list[i][0] + '_' + bed_list[i][1] + '_' + bed_list[i][2]  + '_' + bed_list[i][3]+ '_' + bed_list[i][4])
#        file_output.write('>' + bed_list[i][3])
        file_output.write('>' + bed_list[i][0] + '_' + bed_list[i][1] + '_' + bed_list[i][2] + '_' + bed_list[i][3] + '_' + bed_list[i][4] + '_' + bed_list[i][5] + '_' + bed_list[i][6])
        file_output.write('\n')
        file_output.write(str(record_dict[bed_list[i][0]].seq[int(bed_list[i][1]):int(bed_list[i][2])]))
        file_output.write('\n')
