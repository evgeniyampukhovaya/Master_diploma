# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:37:02 2018

@author: root
"""

import numpy as np
from Bio import SeqIO 
              
                
def site_finder(file_PWM, fasta_file,  file_output, threshold):
    file_PWM=np.loadtxt(file_PWM)
#    print (file_PFM)
    i=0
    wmax=0
    while i<len(file_PWM):
        wmax+=np.max(file_PWM[i])
        i+=1
    wmax=float(wmax)
#    print(wmax)
    i=0
    wmin=0
    while i<len(file_PWM):
        wmin+=np.min(file_PWM[i])
        i+=1
    wmin=float(wmin)
#    print(wmin)
    
    len_file_PWM=len(file_PWM)
    for test_peaks in SeqIO.parse (fasta_file, "fasta"):
        test_peaks=test_peaks.upper()
        i=0
        while i<(len(test_peaks)-len_file_PWM+1):
            window=test_peaks[i:(i+len_file_PWM)]
    #        '+' strand:
            j=0
            windowscore=0
            while j<(len(window)):
                if window[j]=='A':
                    windowscore+=(file_PWM[j,0])
                elif window[j]=='C':
                    windowscore+=(file_PWM[j,1])
                elif window[j]=='G':
                    windowscore+=(file_PWM[j,2])
                elif window[j]=='T':
                    windowscore+=(file_PWM[j,3])
                j+=1    
    #        print (windowscore)
            ws=(windowscore-wmin)/(wmax-wmin)
    #        print(ws)
           
            if ws>=threshold:
                seq=str(test_peaks.seq)
                start=i
                end=i+len_file_PWM-1
                id_seq=test_peaks.name
                print(id_seq)
                window1=str(window.seq)
    #            print(window1)
    #            print(seq)
                file_output.write(str(id_seq)+'\t'+seq+'\t'+str(window1)+'\t'+str(start)+'\t'+str(end)+'\t'+str(ws)+'\t'+'+'+'\n')
    #       '-' strand (coordinates for '+' strand). 
            j=0
            windowscore=0
            while j<(len(window)):
                if window[j]=='T':
                    windowscore+=(file_PWM[len_file_PWM-1-j,0])
                elif window[j]=='G':
                    windowscore+=(file_PWM[len_file_PWM-1-j,1])
                elif window[j]=='C':
                    windowscore+=(file_PWM[len_file_PWM-1-j,2])
                elif window[j]=='A':
                    windowscore+=(file_PWM[len_file_PWM-1-j,3])
                j+=1     
            ws=(windowscore-wmin)/(wmax-wmin)
            if ws>=threshold:
                seq=str(test_peaks.seq)
                start=i
                end=i+len_file_PWM-1
                id_seq=test_peaks.name
                print(id_seq)
                window1=window.reverse_complement()
                window2=str(window1.seq)
    #            print(window1)
    #            print(seq)
                file_output.write(str(id_seq)+'\t'+seq+'\t'+str(window2)+'\t'+str(start)+'\t'+str(end)+'\t'+str(ws)+'\t'+'-'+'\n')
            i+=1
            
     
                
