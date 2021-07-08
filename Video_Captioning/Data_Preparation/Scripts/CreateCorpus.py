# -*- coding: utf-8 -*-
# Author: Adit Goyal
# Date: 2021-06-18

import os
import pandas as pd
import pickle
import numpy as np

#Load the .pkl files prepared earlier.
WordList = pickle.load(open("UCFC-VD_Data_Prep/Files/ucfc-vd_WordList.pkl", "rb"))
SentenceList = pickle.load(open("UCFC-VD_Data_Prep/Files/ucfc-vd_sentence_videoID.pkl", "rb"))

WordList.insert(0,'<eos>')
WordList.insert(1, '<unk>')

#Corpus file with format:
# 0: tokenized train sentences (tokenized sentence, video id)
# 1: tokenized val sentences (tokenized sentence, video id)
# 2: tokenized test sentences (tokenized sentence, video id)
# 3: mapping actual word to index
# 4: mapping index to actual word
# 5: glove embedding per word (300/word)
ucfc_vd_Corpus = []

for i in range(0,3):
    ucfc_vd_Corpus.append([])
ucfc_vd_Corpus.append({})
ucfc_vd_Corpus.append({})

for i in range(0,len(WordList)):
    ucfc_vd_Corpus[3][WordList[i]] = i
for i in range(0,len(WordList)):
    ucfc_vd_Corpus[4][i] = WordList[i]
    
for i in range(0, len(SentenceList[0])):
    SentenceList[0][i] = SentenceList[0][i] + " <eos>"
    SentenceList[0][i] = SentenceList[0][i].split()
    
SentenceList_temp = []

for i in range(0, len(SentenceList[0])):
    SentenceList_temp.append([])
    for j in range (0, len(SentenceList[0][i])):
        SentenceList_temp[i].append(ucfc_vd_Corpus[3][SentenceList[0][i][j].lower()])
        
ucfc_vd_Corpus[0].append([])
ucfc_vd_Corpus[0].append([])
ucfc_vd_Corpus[1].append([])
ucfc_vd_Corpus[1].append([])
ucfc_vd_Corpus[2].append([])
ucfc_vd_Corpus[2].append([])

#To uniformly distribute the video clips from each category, and match the ref files.
for i in range(0, 215):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(0, 215):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(215, 230):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(0, 215):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(230, 250):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(230, 250):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(250, 465):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(250, 465):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(465, 480):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(465, 480):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(480, 500):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(480, 500):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(500, 715):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(500, 715):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(715, 730):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(715, 730):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(730, 750):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(730, 750):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(750, 965):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(750, 965):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(965, 980):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(965, 980):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(980, 1000):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(980, 1000):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(1000, 1430):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(1000, 1430):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(1430, 1460):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(1430, 1460):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(1460, 1500):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(1460, 1500):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(1500, 1715):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(1500, 1715):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(1715, 1730):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(1715, 1730):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(1730, 1750):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(1730, 1750):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(1750, 1965):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(1750, 1965):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(1965, 1980):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(1965, 1980):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(1980, 2000):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(1980, 2000):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(2000, 2645):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(2000, 2645):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(2645, 2690):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(2645, 2690):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(2690, 2750):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(2690, 2750):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(2750, 3395):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(2750, 3395):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(3395, 3440):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(3395, 3440):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(3440, 3500):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(3440, 3500):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(3500, 3715):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(3500, 3715):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(3715, 3730):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(3715, 3730):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(3730, 3750):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(3730, 3750):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(3750, 3965):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(3750, 3965):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(3965, 3980):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(3965, 3980):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(3980, 4000):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(3980, 4000):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(4000, 4430):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(4000, 4430):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(4430, 4460):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(4430, 4460):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(4460, 4500):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(4460, 4500):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
for i in range(4500, 4715):
    ucfc_vd_Corpus[0][0].append(SentenceList_temp[i])
for i in range(4500, 4715):
    ucfc_vd_Corpus[0][1].append(SentenceList[1][i])
for i in range(4715, 4730):
    ucfc_vd_Corpus[1][0].append(SentenceList_temp[i])
for i in range(4715, 4730):
    ucfc_vd_Corpus[1][1].append(SentenceList[1][i])
for i in range(4730, 4750):
    ucfc_vd_Corpus[2][0].append(SentenceList_temp[i])
for i in range(4730, 4750):
    ucfc_vd_Corpus[2][1].append(SentenceList[1][i])
    
#GloVe-840B-300d embeddings to be stored in the Corpus file. Download the .txt file from the official site and upload here.
embeddings_dict = {}
with open("glove.840B.300d.txt", 'r', encoding="utf-8") as f:
    for line in f:
        values = line.split(" ")
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        embeddings_dict[word] = vector

embedding = np.zeros((1589, 300))
i = 0
for key in ucfc_vd_Corpus[3]:
    if i == 0:
        embedding[i] = embeddings_dict['eos']
    elif i == 1:
        embedding[i] = embeddings_dict['unk']
    else:
        try:
            embedding[i] = embeddings_dict[key]
        except KeyError: #For words not present in the GloVe embedding list, create an array of dims 300.
            embedding[i] = np.random.uniform(low = -1, high = 1, size = 300)
    i = i + 1

ucfc_vd_Corpus.append(embedding)

with open("ucfc-vd_Corpus.pkl", 'wb') as fh:
    pickle.dump(ucfc_vd_Corpus, fh)
