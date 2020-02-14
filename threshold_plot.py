# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:04:05 2018

@author: root
"""
import numpy as np
from  matplotlib import pyplot as plt

with open ('FPR_fus3_DAP_seq.txt') as file_thresholds:
    plotfile = np.loadtxt(file_thresholds)
    window_num = plotfile[0]
    plotfile = plotfile/window_num
    x_scale = np.arange(0, 1.0001, 0.0001)
##    plt.scatter(plotfile[:,0], plotfile[:,1], s=10)
    plt.plot(x_scale, plotfile)
    plt.yscale('log')
    plt.xlim(0.7, 1.0)
    plt.ylim(10**(-5), 10**(-1))
    plt.xlabel('thresholds')
    plt.ylabel('FP rate')
    plt.axhline(y=.0001, xmin=0.0, xmax=1.00, linewidth = 1, color = 'red')   
    for i in range (len(plotfile)):
        if plotfile[i] < 0.0001:
            print (i)
            break
    plt.axvline(x = i/10000, ymin = 0.0, ymax = 0.25, linewidth = 1, color = 'red')
    plt.text(x = i/10000, y = 0.0001, s = str(i/10000))
#    plt.show()
#    plt.text(i, 0.25, 'aa'
    plt.savefig('threshold_plot_FUS3_DAP_seq.png', dpi=72)
    plt.savefig('threshold_plot_FUS3_DAP_seq.svg')
##    