from distutils.log import error
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import random
import pandas as pd
import time 
import os
import pathlib
import datetime
import matplotlib.pyplot as plt
from torch import optim
from torch.autograd import Variable 
from pathlib import Path
from random import randint, gauss
import torch.nn as nn
import torch.nn.functional as F
from statistics import mode, mean
import matplotlib.pyplot as plt

directory = 'path'
patient_ID = 'enter list of patients: []'

colums1 = ['time','end time']
colums2 = ['time','end time','Reading 1']
colums3 = ['time','end time','Reading 1','Reading 2']

door_key = 0
switch = 0
pir_key = 0

global Sensor_ID

def Data_Loader(patient):
    sensors_lst = []
    global column_names
    column_names = []
    for subdirectory in os.scandir(directory):
        lock = False
        for patients in os.scandir(subdirectory):
            if str(pathlib.Path(patients)).endswith(patient):
                if lock == False:
                    column_names.append(str(os.path.basename(subdirectory)))
                    lock == True                                              
                sensors = np.load(pathlib.Path(patients))
                sensors_lst.append(sensors)
    sensors_pd = pd.DataFrame([sensors_lst],columns=column_names)
    dataframe_lst = []
    df = pd.DataFrame()
    global sensor_num
    print(len(column_names))
    Sensor_ID = column_names[sensor_num]
    print(Sensor_ID)
    for i in range(len(sensors_pd[Sensor_ID].loc[0])):
        dataframe_lst.append(sensors_pd[Sensor_ID].loc[0][i])
    if len(sensors_pd[Sensor_ID].loc[0][0]) == 2: 
        df = pd.DataFrame(dataframe_lst,columns = colums1)
        df = df.drop("end time", axis=1)
    elif len(sensors_pd[Sensor_ID].loc[0][0]) == 3:    
        df = pd.DataFrame(dataframe_lst,columns = colums2)
        df = df.drop("end time", axis=1)
    elif len(sensors_pd[Sensor_ID].loc[0][0]) == 4:    
        df = pd.DataFrame(dataframe_lst,columns = colums3)
        df = df.drop("end time", axis=1)
    df['labels'] = 0
    delta_t = []
    for i in range(0,len(df)-1):
        delta = abs(df.iloc[i,0] - df.iloc[i+1,0])
        delta_t.append(delta*100)
        i = i+1
    df['time delta'] = pd.Series(delta_t)
    df.dropna(axis=1,inplace=False)
    return df, Sensor_ID
