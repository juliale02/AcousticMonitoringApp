import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import csv
with open('moto1_file_list_machineTime.csv','r') as csvfile1:
    with open('moto_file_list_machineTime.csv','r') as csvfile:
        moto1 = csv.reader(csvfile1, delimiter = '\n')
        moto = csv.reader(csvfile, delimiter = '\n')
        datas = np.zeros([2,200])
        motodata1 = []
        motodata = []
        for row in moto1: 
            motodata1.append(row[0])
        for row in moto: 
            motodata.append(row[0])
        motodata1 = motodata1[:200]
        motodata = motodata[:200]
        datas[0] = motodata1
        datas[1] = motodata
        plt.xlim(left=1663364911507,right=1663384539333)
        colors1 = ['C{}'.format(i) for i in range(2)]
        linelengths1 = [1, 1]
        plt.eventplot(datas, colors=colors1,
            linelengths=linelengths1)
        plt.show()