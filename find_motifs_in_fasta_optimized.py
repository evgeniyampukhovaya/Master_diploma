# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:37:02 2018

@author: root
"""

import numpy as np
from Bio import SeqIO 


         
def site_finder(file_PWM, fasta_file,  file_output, threshold):
    file_PWM=np.loadtxt(file_PWM)

    wmax=sum(np.amax(file_PWM, axis=1))
#    wmax=float(wmax)
    print(wmax)

    wmin=sum(np.amin(file_PWM, axis=1))
#    wmin=float(wmin)
    print(wmin)
    
    len_file_PWM=len(file_PWM)
    count=0
    pwm_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    pwm_dict_rev = {'A':3, 'C':2, 'G':1, 'T':0}
    for test_peaks in SeqIO.parse (fasta_file, "fasta"):
        test_peaks=test_peaks.upper()
#        i=0
        for i in range(len(test_peaks)-len_file_PWM+1):
            window=test_peaks[i:(i+len_file_PWM)].seq
            if window == window.reverse_complement():
                count+=1
            windowscore = 0
            
            
            windowscore_rev = 0
            

            for j in range(len(window)):
                windowscore += file_PWM[j, pwm_dict[window[j]]]
                windowscore_rev += file_PWM[len_file_PWM-1-j, pwm_dict_rev[window[j]]]

            ws = (windowscore-wmin)/(wmax-wmin)
         
            if ws >= threshold:
                seq=str(test_peaks.seq)
                start=i
                end=i+len_file_PWM-1
                id_seq=test_peaks.name
#                print(id_seq)
                window1=str(window)
                file_output.write(str(id_seq)+'\t'+seq+'\t'+(window1)+'\t'+str(start)+'\t'+str(end)+'\t'+str(ws)+'\t'+'+'+'\n')
    #       '-' strand (coordinates for "+" strand)

            ws_rev = (windowscore_rev-wmin)/(wmax-wmin)
            if ws_rev >= threshold:
                seq=str(test_peaks.seq)
                start=i
                end=i+len_file_PWM-1
                id_seq=test_peaks.name
#                print(id_seq)
                window1=window.reverse_complement()
                window2=str(window1)
                file_output.write(str(id_seq)+'\t'+seq+'\t'+(window2)+'\t'+str(start)+'\t'+str(end)+'\t'+str(ws_rev)+'\t'+'-'+'\n')
    print(count)

 
