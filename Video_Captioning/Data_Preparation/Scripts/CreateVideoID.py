# -*- coding: utf-8 -*-
# Author: Adit Goyal
# Date: 2021-06-18

import os
import pandas as pd
import pickle

#Path of the folder containing csv files for captions
folder_path = "UCFC-VD/Captions"

files = os.listdir(folder_path)

j = 0
sentences = []
sentences.append([])
sentences.append([])
for i in range(0, 13):
    file_path = folder_path + "/" + files[i]
    df = pd.read_csv(file_path)
    for i in range(0, len(df['File Name'])):
        sentences[0].append(df['Caption 1'][i])
        sentences[0].append(df['Caption 2'][i])
        sentences[0].append(df['Caption 3'][i])
        sentences[0].append(df['Caption 4'][i])
        sentences[0].append(df['Caption 5'][i])
        
        sentences[1].append(j)
        sentences[1].append(j)
        sentences[1].append(j)
        sentences[1].append(j)
        sentences[1].append(j)
        j = j + 1
        
with open("ucfc-vd_sentence_videoID.pkl", 'wb') as fh:
    pickle.dump(sentences, fh)
