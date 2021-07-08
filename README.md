## Captionomaly: A Deep Learning Toolbox for Anomaly Captioning in Surveillance Videos

### Requirements
python 3.6.9

tensorflow 2.1.3

numpy 1.17.4

cv2 3.4.8

scikit-learn

keras 2.3.1

pycocoevalcap

### Testing

To test the code on individual samples using the weights from the pre-trained model:

1. Extract [C3D features](https://github.com/facebookarchive/C3D) using the given [script](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Anomaly%20Detection/Feature%20Extractor/Feature_Extractor.ipynb) (Ensure dimensions of 240x320 pixels and frame rate of 30 fps).
2. Use the .txt file generated above to get anomaly scores using [Test_Anomaly_Detector_public.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Anomaly%20Detection/Test_Anomaly_Detector_public.py) in the [script](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Anomaly%20Detection/CCTV_Anomaly.ipynb).
3. Use the .txt file generated during the testing with [Save_Anomaly_Clips.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Anomaly%20Detection/Save_Anomaly_Clips.py) to get the anomalous part of the video.
4. Extract frames from the clipped video using [Prepare_frames.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Feature%20Extractor/Prepare_frames.py).
5. Extract [ResNeXt-101 features](https://github.com/taehoonlee/tensornets) for the test video using [generate_res_feature.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Feature%20Extractor/generate_res_feature.py).
6. Use the .npy file generated above to get the tagging vector using [TestTagging.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Tagging%20Network/TestTagging.py).
7. Use the .npy files for ResNext features and Tagging network in the [run_model.sh](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Delving%20Deeper%20into%20the%20Decoder%20for%20Video%20Captioning/run_model.sh).
8. Check the generated caption in the demo log file.

### Training
###### Anomaly Detection 
[Real-World Anomaly Detection in Surveillance Videos](https://github.com/WaqasSultani/AnomalyDetectionCVPR2018)

###### Video Captioning
[Delving Deeper into the Decoder for Video Captioning](https://github.com/WingsBrokenAngel/delving-deeper-into-the-decoder-for-video-captioning#requirement)


1. Prepare the Corpus, Reference, Vocabulary and Tagging files using the scripts given [here](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/tree/main/Video%20Captioning/Data%20Preparation/Scripts).
2. Extract ResNeXt features of all the videos in a single .npy file using [Prepare_frames.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Feature%20Extractor/Prepare_frames.py) and [generate_res_feature.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Feature%20Extractor/generate_res_feature.py).
3. Train the tagging network using [TrainTagNet.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Tagging%20Network/TrainTagNet.py).
4. Test the tagging network to generate a .npy file using [TestTagging.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Tagging%20Network/TestTagging.py).
6. Adjust the configurations for the Captioning model in [config.py](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Delving%20Deeper%20into%20the%20Decoder%20for%20Video%20Captioning/config.py), and train the Captioning model using [run_model.sh](https://github.com/Adit31/Anomaly-Detection-and-Video-Captioning/blob/main/Video%20Captioning/Delving%20Deeper%20into%20the%20Decoder%20for%20Video%20Captioning/run_model.sh).
7. Check the results the train and test log files.
