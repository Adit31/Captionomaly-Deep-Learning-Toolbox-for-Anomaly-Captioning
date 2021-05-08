from moviepy.editor import VideoFileClip

#Path of the video file to be trimmed
InputPath = "C:\\Users\\aditg\\Downloads\\Anomaly-Videos\\Arson\\Arson015_x264.mp4"

#Path of the file to be saved after trimming
OutputPath = "C:\\Users\\aditg\\Downloads\\Anomaly Videos Short\\Arson\\Arson015_x264.mp4"

#Starting time to begin clipping (in seconds)
StartTime = 10

#Ending time to end clipping (in seconds)
EndTime = 35

clip = VideoFileClip(InputPath).subclip(StartTime, EndTime)
clip.to_videofile(OutputPath, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')