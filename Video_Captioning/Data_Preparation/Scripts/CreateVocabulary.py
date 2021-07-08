# -*- coding: utf-8 -*-
# Author: Adit Goyal
# Date: 2021-06-18

import os
import pandas as pd
import pickle

#Folder location of all the Caption Files
folder_path = "UCFC-VD/Captions"

files = os.listdir(folder_path)
word_list = []

for i in range(0, 13):
    file_path = folder_path + "/" + files[i]
    df = pd.read_csv(file_path)
    for i in range(0, len(df['File Name'])):
        sentence1 = df['Caption 1'][i]
        words = sentence1.strip().split()
        for word in words:
            if word.lower() not in word_list:
                word_list.append(word.lower())
        sentence2 = df['Caption 2'][i]
        words = sentence2.strip().split()
        for word in words:
            if word.lower() not in word_list:
                word_list.append(word.lower())
        sentence3 = df['Caption 3'][i]
        words = sentence3.strip().split()
        for word in words:
            if word.lower() not in word_list:
                word_list.append(word.lower())
        sentence4 = df['Caption 4'][i]
        words = sentence4.strip().split()
        for word in words:
            if word.lower() not in word_list:
                word_list.append(word.lower())
        sentence5 = df['Caption 5'][i]
        words = sentence5.strip().split()
        for word in words:
            if word.lower() not in word_list:
                word_list.append(word.lower())

word_list.sort()

with open("ucfc-vd_WordList.pkl", 'wb') as fh:
    pickle.dump(word_list, fh)
