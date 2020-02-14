# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:14:18 2018

@author: root
"""

import numpy as np
#from os import listdir
# Эта функция конвертирует частотную матрицу в весовую по формуле log-odds. Принимает на вход дескрипторы файлов с частотной и весовой матрицей. С частотной открыть в режиме r, с весовой в режиме w
def converter (file_PFM, file_output):
        file_PFM=np.loadtxt(file_PFM)
        print(file_PFM)
        file_PFM=file_PFM*1000000000
        pse=0.25 #псевдокаунты
        pse4=1 #видимо, тоже они
        vych=np.log10(pse)
        for i in range (0, len(file_PFM)):
            summa=np.sum(file_PFM[i])
#            print(summa)
            for j in range (0,4):
                w=((file_PFM[i][j])+pse)/(summa+pse4)
                file_PFM[i][j]=np.log10(w)-vych
        print(file_PFM)
        np.savetxt(file_output, file_PFM,delimiter='\t', fmt='%.10f')

with open('fus3_DAP_PFM.txt', 'r') as file_PFM, open ('fus3_DAP_seq.pwm', 'w' ) as file_output:
    converter (file_PFM, file_output)
#with open ('EIN3_Vlad_new_PFM.motif', 'r') as file_PFM, open ('ein3_new_PWM.txt', 'w') as file_output:
#    converter (file_PFM, file_output)

#for file in listdir(path = 'E:\Work\Распознавание матриц в промоторах генов EIN3 FUS3\PFM'):
##    print (str(file))
#    file_PFM = open(file, 'r')
#    filename = str(file)+'_1'
#    file_out = open (filename, 'w')
#    converter (file_PFM, file_out)
    