from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor
import os
from os import listdir
from os.path import isfile, join

#Path of Directory containing the videos (.mp4) for anomaly detection
test_videoClips_path = '/content/drive/MyDrive/AnomalyDetectionCVPR2018/SampleVideoClips'
#Path of Directory containing anomaly score files (.txt) for each video used in anomaly detection
eval_res_path = '/content/drive/MyDrive/Eval_Res'
#Path of Directory to store the clipped videos
Results_Path = "/content/drive/MyDrive/AnomalyDetectionCVPR2018/AnomalyClips/"

if not os.path.exists(Results_Path):
    os.makedirs(Results_Path)

All_eval_files = listdir(eval_res_path)
All_test_videoClips = listdir(test_videoClips_path)

All_eval_files.sort()
All_test_videoClips.sort()

#Threshold Value above which we consider the score as anomalous
threshold = 0.5

for i in range(len(All_eval_files)):
  eval_file_path = os.path.join(eval_res_path, All_eval_files[i])
  video_file_path = os.path.join(test_videoClips_path, All_test_videoClips[i])
  eval_file = open(eval_file_path, 'r')
  video_file = moviepy.editor.VideoFileClip(video_file_path)
  aa=All_eval_files[i]
  aa=aa[0:-4]
  video_duration = int(video_file.duration)
  Each_segment_length = video_duration//32

  j = 1
  for each in eval_file:
    Seg_score = float(each)
    if Seg_score >= threshold:
      if j == 1:
        Anomaly_startTime = 0
      else:
        Anomaly_startTime = Each_segment_length * (j - 1.15)
            
      if j == 32:
        Anomaly_endTime = video_duration
      else:
        Anomaly_endTime = Each_segment_length * (j + 0.15)
      print(Anomaly_endTime)
      print(Anomaly_startTime)
      ffmpeg_extract_subclip(video_file_path, Anomaly_startTime, Anomaly_endTime, targetname= Results_Path + aa + "_" + str(j) + ".mp4")
    j = j + 1
