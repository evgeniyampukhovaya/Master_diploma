# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:39:41 2019

@author: puhovajaem
"""

def intersections_peak_promoter (file_peak, file_annotation, file_out):
    for line1 in file_peak:
        line1 = line1.strip('\n')
        line1 = line1.split('\t')
        start_peak = int(line1[1])
        end_peak = int(line1[2])
        chromosome_peak = int(line1[0])
#        print (chromosome_peak)
        for line2 in file_annotation:
            line2 = line2.strip('\n')
            line2 = line2.split('\t')      
            start_promoter = int(line2[1])
            end_promoter = int(line2[2])
            chromosome_promoter = int(line2[0])
#            print (chromosome_promoter)
            gene_name = line2[3]
            gene_strain = line2[4]
            if chromosome_peak == chromosome_promoter:
#                print(c1)
                if ((start_promoter < start_peak < end_promoter) or (start_promoter < end_peak < end_promoter)):
                    file_out.write(str(chromosome_peak)+'\t'+str(start_peak)+'\t'+str(end_peak)+'\t'+str(gene_name)+'\t'+str(gene_strain) +'\t'+str(start_promoter)+'\t'+str(end_promoter)+'\n')
        file_annotation.seek(0)
        
with open ('EIN3_timeseries_12_with_input_control.bed') as file_peak, open ('C:/Users/puhovajaem/Работа/FUS3_new_data/motif_to_PWM_and_threshold/Araport11_201606_prot_cod_gene_promoters_1500_longest_UTR_strain.bed') as file_annotation, open ('genes_EIN3_timeseries_12_with_input_control.bed', 'w') as file_out:
    intersections_peak_promoter (file_peak, file_annotation, file_out)