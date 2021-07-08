# -*- coding: utf-8 -*-
# Author: Adit Goyal
# Date: 2021-06-18

import pandas as pd
import glob
import os

#Path of the location captions files are saved
#Abuse
Caption_CSV_Path = "/home/users/multicog/Adit/UCFC-VD/Captions/Abuse.csv"
df = pd.read_csv(Caption_CSV_Path)
Caption_List = []

for i in range(0,3):
    Caption_List.append([])
    
#Training
for i in range(0, 43):
    Caption_List[0].append([])
for i in range(0, 43):
    Caption_List[0][i].append(df["Caption 1"][i])
    Caption_List[0][i].append(df["Caption 2"][i])
    Caption_List[0][i].append(df["Caption 3"][i])
    Caption_List[0][i].append(df["Caption 4"][i])
    Caption_List[0][i].append(df["Caption 5"][i])
    
#Validation
for i in range(0, 3):
    Caption_List[1].append([])
j = 0
for i in range(43, 46):
    Caption_List[1][j].append(df["Caption 1"][i])
    Caption_List[1][j].append(df["Caption 2"][i])
    Caption_List[1][j].append(df["Caption 3"][i])
    Caption_List[1][j].append(df["Caption 4"][i])
    Caption_List[1][j].append(df["Caption 5"][i])
    j = j + 1

#Testing
for i in range(0, 4):
    Caption_List[2].append([])
j = 0
for i in range(46, 50):
    Caption_List[2][j].append(df["Caption 1"][i])
    Caption_List[2][j].append(df["Caption 2"][i])
    Caption_List[2][j].append(df["Caption 3"][i])
    Caption_List[2][j].append(df["Caption 4"][i])
    Caption_List[2][j].append(df["Caption 5"][i])
    j = j + 1
    
#Arrest
Caption_CSV_Path_2 = "/home/users/multicog/Adit/UCFC-VD/Captions/Arrest.csv"

df2 = pd.read_csv(Caption_CSV_Path_2)
#Training
for i in range(0, 43):
    Caption_List[0].append([])
for i in range(0, 43):
    Caption_List[0][43+i].append(df2["Caption 1"][i])
    Caption_List[0][43+i].append(df2["Caption 2"][i])
    Caption_List[0][43+i].append(df2["Caption 3"][i])
    Caption_List[0][43+i].append(df2["Caption 4"][i])
    Caption_List[0][43+i].append(df2["Caption 5"][i])
    
#Validation
for i in range(0, 3):
    Caption_List[1].append([])
j = 0
for i in range(43, 46):
    Caption_List[1][3+j].append(df2["Caption 1"][i])
    Caption_List[1][3+j].append(df2["Caption 2"][i])
    Caption_List[1][3+j].append(df2["Caption 3"][i])
    Caption_List[1][3+j].append(df2["Caption 4"][i])
    Caption_List[1][3+j].append(df2["Caption 5"][i])
    j = j + 1

#Testing
for i in range(0, 4):
    Caption_List[2].append([])
j = 0
for i in range(46, 50):
    Caption_List[2][4+j].append(df2["Caption 1"][i])
    Caption_List[2][4+j].append(df2["Caption 2"][i])
    Caption_List[2][4+j].append(df2["Caption 3"][i])
    Caption_List[2][4+j].append(df2["Caption 4"][i])
    Caption_List[2][4+j].append(df2["Caption 5"][i])
    j = j + 1
    
#Arson
Caption_CSV_Path_3 = "/home/users/multicog/Adit/UCFC-VD/Captions/Arson.csv"

df3 = pd.read_csv(Caption_CSV_Path_3)
#Training
for i in range(0, 43):
    Caption_List[0].append([])
for i in range(0, 43):
    Caption_List[0][86+i].append(df3["Caption 1"][i])
    Caption_List[0][86+i].append(df3["Caption 2"][i])
    Caption_List[0][86+i].append(df3["Caption 3"][i])
    Caption_List[0][86+i].append(df3["Caption 4"][i])
    Caption_List[0][86+i].append(df3["Caption 5"][i])
    
#Validation
for i in range(0, 3):
    Caption_List[1].append([])
j = 0
for i in range(43, 46):
    Caption_List[1][6+j].append(df3["Caption 1"][i])
    Caption_List[1][6+j].append(df3["Caption 2"][i])
    Caption_List[1][6+j].append(df3["Caption 3"][i])
    Caption_List[1][6+j].append(df3["Caption 4"][i])
    Caption_List[1][6+j].append(df3["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 4):
    Caption_List[2].append([])
j = 0
for i in range(46, 50):
    Caption_List[2][8+j].append(df3["Caption 1"][i])
    Caption_List[2][8+j].append(df3["Caption 2"][i])
    Caption_List[2][8+j].append(df3["Caption 3"][i])
    Caption_List[2][8+j].append(df3["Caption 4"][i])
    Caption_List[2][8+j].append(df3["Caption 5"][i])
    j = j + 1
    
#Assault
Caption_CSV_Path_4 = "/home/users/multicog/Adit/UCFC-VD/Captions/Assault.csv"

df4 = pd.read_csv(Caption_CSV_Path_4)
#Training
for i in range(0, 43):
    Caption_List[0].append([])
for i in range(0, 43):
    Caption_List[0][129+i].append(df4["Caption 1"][i])
    Caption_List[0][129+i].append(df4["Caption 2"][i])
    Caption_List[0][129+i].append(df4["Caption 3"][i])
    Caption_List[0][129+i].append(df4["Caption 4"][i])
    Caption_List[0][129+i].append(df4["Caption 5"][i])
    
#Validation
for i in range(0, 3):
    Caption_List[1].append([])
j = 0
for i in range(43, 46):
    Caption_List[1][9+j].append(df4["Caption 1"][i])
    Caption_List[1][9+j].append(df4["Caption 2"][i])
    Caption_List[1][9+j].append(df4["Caption 3"][i])
    Caption_List[1][9+j].append(df4["Caption 4"][i])
    Caption_List[1][9+j].append(df4["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 4):
    Caption_List[2].append([])
j = 0
for i in range(46, 50):
    Caption_List[2][12+j].append(df4["Caption 1"][i])
    Caption_List[2][12+j].append(df4["Caption 2"][i])
    Caption_List[2][12+j].append(df4["Caption 3"][i])
    Caption_List[2][12+j].append(df4["Caption 4"][i])
    Caption_List[2][12+j].append(df4["Caption 5"][i])
    j = j + 1
    
#Burglary
Caption_CSV_Path_5 = "/home/users/multicog/Adit/UCFC-VD/Captions/Burglary.csv"

df5 = pd.read_csv(Caption_CSV_Path_5)
#Training
for i in range(0, 86):
    Caption_List[0].append([])
for i in range(0, 86):
    Caption_List[0][172+i].append(df5["Caption 1"][i])
    Caption_List[0][172+i].append(df5["Caption 2"][i])
    Caption_List[0][172+i].append(df5["Caption 3"][i])
    Caption_List[0][172+i].append(df5["Caption 4"][i])
    Caption_List[0][172+i].append(df5["Caption 5"][i])
    
#Validation
for i in range(0, 6):
    Caption_List[1].append([])
j = 0
for i in range(86, 92):
    Caption_List[1][12+j].append(df5["Caption 1"][i])
    Caption_List[1][12+j].append(df5["Caption 2"][i])
    Caption_List[1][12+j].append(df5["Caption 3"][i])
    Caption_List[1][12+j].append(df5["Caption 4"][i])
    Caption_List[1][12+j].append(df5["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 8):
    Caption_List[2].append([])
j = 0
for i in range(92, 100):
    Caption_List[2][16+j].append(df5["Caption 1"][i])
    Caption_List[2][16+j].append(df5["Caption 2"][i])
    Caption_List[2][16+j].append(df5["Caption 3"][i])
    Caption_List[2][16+j].append(df5["Caption 4"][i])
    Caption_List[2][16+j].append(df5["Caption 5"][i])
    j = j + 1
    
#Explosion
Caption_CSV_Path_6 = "/home/users/multicog/Adit/UCFC-VD/Captions/Explosion.csv"

df6 = pd.read_csv(Caption_CSV_Path_6)
#Training
for i in range(0, 43):
    Caption_List[0].append([])
for i in range(0, 43):
    Caption_List[0][258+i].append(df6["Caption 1"][i])
    Caption_List[0][258+i].append(df6["Caption 2"][i])
    Caption_List[0][258+i].append(df6["Caption 3"][i])
    Caption_List[0][258+i].append(df6["Caption 4"][i])
    Caption_List[0][258+i].append(df6["Caption 5"][i])
    
#Validation
for i in range(0, 3):
    Caption_List[1].append([])
j = 0
for i in range(43, 46):
    Caption_List[1][18+j].append(df6["Caption 1"][i])
    Caption_List[1][18+j].append(df6["Caption 2"][i])
    Caption_List[1][18+j].append(df6["Caption 3"][i])
    Caption_List[1][18+j].append(df6["Caption 4"][i])
    Caption_List[1][18+j].append(df6["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 4):
    Caption_List[2].append([])
j = 0
for i in range(46, 50):
    Caption_List[2][24+j].append(df6["Caption 1"][i])
    Caption_List[2][24+j].append(df6["Caption 2"][i])
    Caption_List[2][24+j].append(df6["Caption 3"][i])
    Caption_List[2][24+j].append(df6["Caption 4"][i])
    Caption_List[2][24+j].append(df6["Caption 5"][i])
    j = j + 1
    
#Fighting
Caption_CSV_Path_7 = "/home/users/multicog/Adit/UCFC-VD/Captions/Fighting.csv"

df7 = pd.read_csv(Caption_CSV_Path_7)
#Training
for i in range(0, 43):
    Caption_List[0].append([])
for i in range(0, 43):
    Caption_List[0][301+i].append(df7["Caption 1"][i])
    Caption_List[0][301+i].append(df7["Caption 2"][i])
    Caption_List[0][301+i].append(df7["Caption 3"][i])
    Caption_List[0][301+i].append(df7["Caption 4"][i])
    Caption_List[0][301+i].append(df7["Caption 5"][i])
    
#Validation
for i in range(0, 3):
    Caption_List[1].append([])
j = 0
for i in range(43, 46):
    Caption_List[1][21+j].append(df7["Caption 1"][i])
    Caption_List[1][21+j].append(df7["Caption 2"][i])
    Caption_List[1][21+j].append(df7["Caption 3"][i])
    Caption_List[1][21+j].append(df7["Caption 4"][i])
    Caption_List[1][21+j].append(df7["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 4):
    Caption_List[2].append([])
j = 0
for i in range(46, 50):
    Caption_List[2][28+j].append(df7["Caption 1"][i])
    Caption_List[2][28+j].append(df7["Caption 2"][i])
    Caption_List[2][28+j].append(df7["Caption 3"][i])
    Caption_List[2][28+j].append(df7["Caption 4"][i])
    Caption_List[2][28+j].append(df7["Caption 5"][i])
    j = j + 1
    
#RoadAccidents
Caption_CSV_Path_8 = "/home/users/multicog/Adit/UCFC-VD/Captions/RoadAccidents.csv"

df8 = pd.read_csv(Caption_CSV_Path_8)
#Training
for i in range(0, 129):
    Caption_List[0].append([])
for i in range(0, 129):
    Caption_List[0][344+i].append(df8["Caption 1"][i])
    Caption_List[0][344+i].append(df8["Caption 2"][i])
    Caption_List[0][344+i].append(df8["Caption 3"][i])
    Caption_List[0][344+i].append(df8["Caption 4"][i])
    Caption_List[0][344+i].append(df8["Caption 5"][i])
    
#Validation
for i in range(0, 9):
    Caption_List[1].append([])
j = 0
for i in range(129, 138):
    Caption_List[1][24+j].append(df8["Caption 1"][i])
    Caption_List[1][24+j].append(df8["Caption 2"][i])
    Caption_List[1][24+j].append(df8["Caption 3"][i])
    Caption_List[1][24+j].append(df8["Caption 4"][i])
    Caption_List[1][24+j].append(df8["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 12):
    Caption_List[2].append([])
j = 0
for i in range(138, 150):
    Caption_List[2][32+j].append(df8["Caption 1"][i])
    Caption_List[2][32+j].append(df8["Caption 2"][i])
    Caption_List[2][32+j].append(df8["Caption 3"][i])
    Caption_List[2][32+j].append(df8["Caption 4"][i])
    Caption_List[2][32+j].append(df8["Caption 5"][i])
    j = j + 1
    
#Robbery
Caption_CSV_Path_9 = "/home/users/multicog/Adit/UCFC-VD/Captions/Robbery.csv"

df9 = pd.read_csv(Caption_CSV_Path_9)
#Training
for i in range(0, 129):
    Caption_List[0].append([])
for i in range(0, 129):
    Caption_List[0][473+i].append(df9["Caption 1"][i])
    Caption_List[0][473+i].append(df9["Caption 2"][i])
    Caption_List[0][473+i].append(df9["Caption 3"][i])
    Caption_List[0][473+i].append(df9["Caption 4"][i])
    Caption_List[0][473+i].append(df9["Caption 5"][i])
    
#Validation
for i in range(0, 9):
    Caption_List[1].append([])
j = 0
for i in range(129, 138):
    Caption_List[1][33+j].append(df9["Caption 1"][i])
    Caption_List[1][33+j].append(df9["Caption 2"][i])
    Caption_List[1][33+j].append(df9["Caption 3"][i])
    Caption_List[1][33+j].append(df9["Caption 4"][i])
    Caption_List[1][33+j].append(df9["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 12):
    Caption_List[2].append([])
j = 0
for i in range(138, 150):
    Caption_List[2][44+j].append(df9["Caption 1"][i])
    Caption_List[2][44+j].append(df9["Caption 2"][i])
    Caption_List[2][44+j].append(df9["Caption 3"][i])
    Caption_List[2][44+j].append(df9["Caption 4"][i])
    Caption_List[2][44+j].append(df9["Caption 5"][i])
    j = j + 1
    
#Shooting
Caption_CSV_Path_10 = "/home/users/multicog/Adit/UCFC-VD/Captions/Shooting.csv"

df10 = pd.read_csv(Caption_CSV_Path_10)
#Training
for i in range(0, 43):
    Caption_List[0].append([])
for i in range(0, 43):
    Caption_List[0][602+i].append(df10["Caption 1"][i])
    Caption_List[0][602+i].append(df10["Caption 2"][i])
    Caption_List[0][602+i].append(df10["Caption 3"][i])
    Caption_List[0][602+i].append(df10["Caption 4"][i])
    Caption_List[0][602+i].append(df10["Caption 5"][i])
    
#Validation
for i in range(0, 3):
    Caption_List[1].append([])
j = 0
for i in range(43, 46):
    Caption_List[1][42+j].append(df10["Caption 1"][i])
    Caption_List[1][42+j].append(df10["Caption 2"][i])
    Caption_List[1][42+j].append(df10["Caption 3"][i])
    Caption_List[1][42+j].append(df10["Caption 4"][i])
    Caption_List[1][42+j].append(df10["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 4):
    Caption_List[2].append([])
j = 0
for i in range(46, 50):
    Caption_List[2][56+j].append(df10["Caption 1"][i])
    Caption_List[2][56+j].append(df10["Caption 2"][i])
    Caption_List[2][56+j].append(df10["Caption 3"][i])
    Caption_List[2][56+j].append(df10["Caption 4"][i])
    Caption_List[2][56+j].append(df10["Caption 5"][i])
    j = j + 1
    
#Shoplifting
Caption_CSV_Path_11 = "/home/users/multicog/Adit/UCFC-VD/Captions/Shoplifting.csv"

df11 = pd.read_csv(Caption_CSV_Path_11)
#Training
for i in range(0, 43):
    Caption_List[0].append([])
for i in range(0, 43):
    Caption_List[0][645+i].append(df11["Caption 1"][i])
    Caption_List[0][645+i].append(df11["Caption 2"][i])
    Caption_List[0][645+i].append(df11["Caption 3"][i])
    Caption_List[0][645+i].append(df11["Caption 4"][i])
    Caption_List[0][645+i].append(df11["Caption 5"][i])
    
#Validation
for i in range(0, 3):
    Caption_List[1].append([])
j = 0
for i in range(43, 46):
    Caption_List[1][45+j].append(df11["Caption 1"][i])
    Caption_List[1][45+j].append(df11["Caption 2"][i])
    Caption_List[1][45+j].append(df11["Caption 3"][i])
    Caption_List[1][45+j].append(df11["Caption 4"][i])
    Caption_List[1][45+j].append(df11["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 4):
    Caption_List[2].append([])
j = 0
for i in range(46, 50):
    Caption_List[2][60+j].append(df11["Caption 1"][i])
    Caption_List[2][60+j].append(df11["Caption 2"][i])
    Caption_List[2][60+j].append(df11["Caption 3"][i])
    Caption_List[2][60+j].append(df11["Caption 4"][i])
    Caption_List[2][60+j].append(df11["Caption 5"][i])
    j = j + 1
    
#Stealing
Caption_CSV_Path_12 = "/home/users/multicog/Adit/UCFC-VD/Captions/Stealing.csv"

df12 = pd.read_csv(Caption_CSV_Path_12)
#Training
for i in range(0, 86):
    Caption_List[0].append([])
for i in range(0, 86):
    Caption_List[0][688+i].append(df12["Caption 1"][i])
    Caption_List[0][688+i].append(df12["Caption 2"][i])
    Caption_List[0][688+i].append(df12["Caption 3"][i])
    Caption_List[0][688+i].append(df12["Caption 4"][i])
    Caption_List[0][688+i].append(df12["Caption 5"][i])
    
#Validation
for i in range(0, 6):
    Caption_List[1].append([])
j = 0
for i in range(86, 92):
    Caption_List[1][48+j].append(df12["Caption 1"][i])
    Caption_List[1][48+j].append(df12["Caption 2"][i])
    Caption_List[1][48+j].append(df12["Caption 3"][i])
    Caption_List[1][48+j].append(df12["Caption 4"][i])
    Caption_List[1][48+j].append(df12["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 8):
    Caption_List[2].append([])
j = 0
for i in range(92, 100):
    Caption_List[2][64+j].append(df12["Caption 1"][i])
    Caption_List[2][64+j].append(df12["Caption 2"][i])
    Caption_List[2][64+j].append(df12["Caption 3"][i])
    Caption_List[2][64+j].append(df12["Caption 4"][i])
    Caption_List[2][64+j].append(df12["Caption 5"][i])
    j = j + 1
    
#Vandalism
Caption_CSV_Path_13 = "/home/users/multicog/Adit/UCFC-VD/Captions/Vandalism.csv"

df13 = pd.read_csv(Caption_CSV_Path_13)
#Training
for i in range(0, 43):
    Caption_List[0].append([])
for i in range(0, 43):
    Caption_List[0][774+i].append(df13["Caption 1"][i])
    Caption_List[0][774+i].append(df13["Caption 2"][i])
    Caption_List[0][774+i].append(df13["Caption 3"][i])
    Caption_List[0][774+i].append(df13["Caption 4"][i])
    Caption_List[0][774+i].append(df13["Caption 5"][i])
    
#Validation
for i in range(0, 3):
    Caption_List[1].append([])
j = 0
for i in range(43, 46):
    Caption_List[1][54+j].append(df13["Caption 1"][i])
    Caption_List[1][54+j].append(df13["Caption 2"][i])
    Caption_List[1][54+j].append(df13["Caption 3"][i])
    Caption_List[1][54+j].append(df13["Caption 4"][i])
    Caption_List[1][54+j].append(df13["Caption 5"][i])
    j = j + 1
    
#Testing
for i in range(0, 4):
    Caption_List[2].append([])
j = 0
for i in range(46, 50):
    Caption_List[2][72+j].append(df13["Caption 1"][i])
    Caption_List[2][72+j].append(df13["Caption 2"][i])
    Caption_List[2][72+j].append(df13["Caption 3"][i])
    Caption_List[2][72+j].append(df13["Caption 4"][i])
    Caption_List[2][72+j].append(df13["Caption 5"][i])
    j = j + 1
    
with open("ucfc-vd_ref.pkl", 'wb') as fh:
    pickle.dump(Caption_List, fh)
