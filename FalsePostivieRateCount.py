# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:37:02 2018

@author: root
"""

import numpy as np
from Bio import SeqIO 
from math import floor
from timeit import default_timer
         
def site_finder(file_PWM, fasta_file, file_output):
    file_PWM = np.loadtxt(file_PWM)

    wmax = sum(np.amax(file_PWM, axis=1))
    wmax = float(wmax)
    print(wmax)

    wmin = sum(np.amin(file_PWM, axis=1))
    wmin = float(wmin)
    print(wmin)
    
    len_file_PWM = len(file_PWM)

    scores = np.arange(0, 10001, 1)
    scores[:] = 0
    pwm_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    N_count = 0
    for test_peaks in SeqIO.parse (fasta_file, "fasta"):
        N = False
        st = default_timer() 
        test_peaks = test_peaks.upper()
#        i=0
        print(test_peaks.name)
        test_peaks = str(test_peaks.seq)
        test_peaks = test_peaks.upper()
#        print(type(test_peaks[1:10]))
        for i in range(len(test_peaks)-len_file_PWM+1):
            window = test_peaks[i:(i+len_file_PWM)]
#            if window == window.reverse_complement():

            windowscore = 0
            
            for j in range(len(window)):
                try:
                    windowscore += file_PWM[j, pwm_dict[window[j]]]
                except KeyError:
                    print('Find N')
                    N_count += 1
                    N = True
                    break
#                    j += j+len_file_PWM

            if (not N):
                ws = (windowscore-wmin)/(wmax-wmin)*10000
#                print(window)
#                print(ws)
#                round_score =  round(ws, 5)*10000
                round_score = floor(ws)
#                print(round_score)
#            print(scores)
#                print(int(round_score))
#                print(scores[0:int(round_score)])
                scores[0:int(round_score)] += int(1)
#        print(scores)
            N = False
        print(default_timer() - st)
   
#    file_output.writelines(scores)
    print(scores)
    print (N_count)
    file_output.writelines('\t'.join(map(str, list(scores))))
    file_output.writelines('\n')
start = default_timer() 
    
with open('fus3_DAP_seq.pwm', 'r') as file_PWM, open ('Araport11_201606_prot_cod_gene_promoters_1500_longest_UTR.fasta', 'r') as fasta_file, open ('FPR_fus3_DAP_seq.txt', 'w') as file_output: 
     site_finder(file_PWM, fasta_file,  file_output)

end = default_timer() - start
