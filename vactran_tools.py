"""
Owner: M. Sung

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# GLOBAL
COLOR = ['red', 'blue', 'green','olive','cyan',
              'darkorange', 'black', 'darkviolet']


# input file name and returns the dataframe
def read_data(filename, xlabel, ylabel):
    header = ['label', 'number', xlabel, ylabel]
    df = pd.read_table(filename, header=None, names=header, 
                       sep="\t", encoding="utf_16_le")
    return df

def assign_plot2(df, resolution, xlabel, ylabel, loglog):
    l1 = df.iloc[0, 0]
    l2 = df.iloc[resolution, 0]
    x1 = df.iloc[:resolution, 2]
    x2 = df.iloc[:resolution, 3]
    y1 = df.iloc[resolution:, 2]
    y2 = df.iloc[resolution:, 3]
     
        
    plt.figure(figsize=(18,14))
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    # plt.legend(fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(which='both')
    
    if loglog:
        plt.loglog(x1, y1, color=COLOR[0], label=l1)
        plt.loglog(x2, y2, color=COLOR[1], label=l2)
        
    else:
        plt.plot(x1, y1, color=COLOR[0], label=l1)
        plt.plot(x2, y2, color=COLOR[1], label=l2)   
    
    plt.legend(fontsize=15)
    plt.show()
    
def assign_plot(df, xlabel, ylabel, data_label, color_code, loglog):
    x1 = df.iloc[:, 2]
    y1 = df.iloc[:, 3]
        
    
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    # plt.legend(fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    
    if loglog:
        plt.loglog(x1, y1, color=COLOR[color_code], label=data_label)
        
    else:
        plt.plot(x1, y1, color=COLOR[color_code], label=data_label)
    
    plt.legend(fontsize=12)
    
    
            
# input list of files to compare, use same xlabel ylabel
def compare_cond(filelist, xlabel, ylabel, loglog):
    #num_color = len(filelist)
    plt.figure(figsize=(18,14))
    
    for i, fname in enumerate(filelist):
        df = read_data(fname, xlabel, ylabel)
        dname = fname.strip('.dat')
        assign_plot(df, xlabel, ylabel, dname, i, loglog)
    
    plt.ion()
    plt.grid(which='both')
    plt.show()


        
        
        
