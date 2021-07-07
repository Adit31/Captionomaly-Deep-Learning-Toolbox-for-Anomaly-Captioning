# -*- coding: utf-8 -*-
# Author: Adit Goyal
# Date: 2021-06-18

"""This is the script used to generate UCFC-VD features"""

import cv2
import numpy as np
#import tensorflow as tf
import tensorflow.compat.v1 as tf
import tensornets as nets
from tensornets.utils import load_img
import math
import scipy.io as sio
import time
import random
import itertools
import os
from pprint import pprint
import pickle
import glob
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers import AveragePooling3D

tf.compat.v1.disable_eager_execution()

batch_size = 32
seg_size = 32
dims = [batch_size, 224, 224, 3]
no_of_videos = 950
global flags


def generate_feat(inputx, model, out_feats, sess):
    """Use the imgload that comes with the model to read the image of each video
    Then use the model to process these images to get the output characteristics
    Finally save these features as a file in npy format
    """
    # Import video list
    global flags
    seg_name = os.path.basename(flags.input)
    vid_names = glob.glob(os.path.join(flags.input, '*'))
    res_feats = np.zeros([no_of_videos, seg_size, 2048], np.float32)
    # Read seg_size pictures evenly for each video, and process one video as a batch
    for idx, vid_n in enumerate(vid_names):
        # Read in all the picture names of the video and select seg_size pictures evenly
        input_imgs = np.zeros(shape=dims, dtype=np.float32)
        vid_idx = int(os.path.basename(vid_n)[:])
        fpaths = glob.glob(os.path.join(vid_n, '*'))
        frm_len = len(fpaths)
        if frm_len == 0:
            continue
        delta = frm_len / seg_size
        idx_list = [int(i*delta) for i in range(seg_size)]
        print(idx, vid_n, frm_len, max(idx_list))
        # Use load_img to read the images in the list, and model.preprocess for preprocessing
        for idx2, idx3 in enumerate(idx_list):
            img_path = fpaths[idx3]
            img = load_img(img_path, target_size=256, crop_size=224)
            input_imgs[idx2,:,:,:] = model.preprocess(img)

        feats = sess.run(out_feats, {inputx: input_imgs})

        res_feats[vid_idx] = feats
        print(idx, 'video has been processed.')
    np.save(flags.output, res_feats)
    
    res_feats = res_feats.reshape(1, no_of_videos, 32, 2048, 1)
    model = Sequential([AveragePooling3D(pool_size = (1, 32, 1))])
    resnet_avg = model.predict(res_feats)
    resnet_avg = np.squeeze(resnet_avg)
        
    min_max_scaler = preprocessing.MinMaxScaler()
    scaled_resnet = min_max_scaler.fit_transform(resnet_avg.reshape(-1,no_of_videos))
    scaled_resnet = scaled_resnet.reshape(no_of_videos,-1))
    np.save(flags.scaled_output, scaled_resnet)



if __name__ == "__main__":
    global flags
    #Directory address to read the frames
    tf.app.flags.DEFINE_string('input', '/home/users/multicog/Adit/Anomaly_temp/Frames', 'input path')  
    #Address where npy file has to be saved 
    tf.app.flags.DEFINE_string('output', '/home/users/multicog/Adit/ResnetFeatures/ResNeXt', 'output path')  
    tf.app.flags.DEFINE_string('scaled_output', '/home/users/multicog/Adit/ResnetFeatures/Scaled_ResNeXt', 'scaled output path')
    flags = tf.app.flags.FLAGS
    # Model file
    inputx = tf.placeholder(tf.float32, [None, 224, 224, 3])
    model = nets.ResNeXt101c64(inputx, is_training=False)
    out_feats = model.get_outputs()[-3]
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)
    sess.run(tf.global_variables_initializer())
    sess.run(model.pretrained())
    # Feature
    generate_feat(inputx, model, out_feats, sess)
