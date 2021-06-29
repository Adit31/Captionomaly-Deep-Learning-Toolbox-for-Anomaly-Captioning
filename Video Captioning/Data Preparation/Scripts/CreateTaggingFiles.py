# -*- coding: utf-8 -*-
# Author: Adit Goyal
# Date: 2021-06-18

import pickle
import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer

#Path to the Corpus file
CorpusFile = "UCFC-VD_Data_Prep/Files/ucfc-vd_Corpus.pkl"

#Path to the Ref file
RefFile = "UCFC-VD_Data_Prep/Files/ucfc-vd_ref.pkl"

#Path to the Sentence-VideoID file
sentence_videoID = "UCFC-VD_Data_Prep/Files/ucfc-vd_sentence_videoID.pkl"

#Dimensions of tag_gt: [no. of videos, no. of labels]
tag_gt = np.zeros([950, 300], np.int32)

with open(CorpusFile, 'rb') as fo:
    data = pickle.load(fo)
    train, val, test = data[0], data[1], data[2]
    word2idx, idx2word = data[3], data[4]
    n_v = len(idx2word)
    counter = np.zeros([n_v], np.int32)
    for sent in train[0]:
        for w in sent:
            counter[w] += 1

    for sent in val[0]:
        for w in sent:
            counter[w] += 1

    indices = np.argsort(counter)[::-1]

    counter_sorted = np.sort(counter)[::-1]

    word_sorted = []
    for i in indices:
        word_sorted.append(idx2word[i])

sentences = pickle.load(open(RefFile, 'rb'))
sentences_list = []
for i in sentences[0]+sentences[1]:
    for j in i:
        sentences_list.append(j)

#Tokenization to create labels
string = ""
for i in sentences_list:
    string = string + " " + i

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(string)
word_tokens = [w.strip() for w in word_tokens]
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        if len(w) > 2:    #To remove insignificant words missed by the stopwords above
            filtered_sentence.append(w)

#Finding the most common words in the dataset to create labels
df1 = pd.Series(filtered_sentence).value_counts().sort_index().reset_index().reset_index(drop=True)
df1.columns = ['Element', 'Frequency']
df2 = df1.sort_values('Frequency', ascending = False)

words = list(df2['Element'])
final_words = []

#Will pick 300 labels manually from the words list
words = words[:400]
for word in words:
    print(word)
    x = input("Do you want it? ")
    if x == 'y':
        final_words.append(word)
    if len(final_words) == 300:
        break
        
idx2word_tag, word2idx_tag = {}, {}

for idx, word in enumerate(final_words):
    idx2word_tag[idx] = word
    word2idx_tag[word] = idx

with open("ucfc-vd_tag_idx_word.pkl", "wb") as fo:
    pickle.dump([idx2word_tag, word2idx_tag], fo, -1)

#Creating .npy tag file for the tagging network
sentence_id = pickle.load(open(sentence_videoID, "rb"))
tokenizer = TreebankWordTokenizer()

for i in range(0, len(sentence_id[0])):
    sentence = sentence_id[0][i]
    video_id = sentence_id[1][i]
    words = tokenizer.tokenize(sentence)
    for word in words:
        if word in word2idx_tag:
            tag_gt[video_id, word2idx_tag[word]] = 1

np.save('ucfc-vd_tag_gt', tag_gt)
