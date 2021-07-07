# -*- coding: utf-8 -*-
# Author: Adit Goyal
# Date: 2021-06-18

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import pickle
import numpy as np
import sys
from pprint import pprint
from collections import defaultdict
import time
sys.path.append('..')
from utils import *


np.random.seed(42)
data_dict = None
model = None
options = None

METRICS = {'Bleu_4': 0., 'CIDEr': 0., 
           'METEOR': 0., 'ROUGE_L': 0.}
MAX = {key: 0. for key in METRICS}
min_xe = 100000

def cal_metrics(sess, phase):
    sent_dict, sent_list = defaultdict(list), []
    loss_list = []
    ''' Mapping idx_range for train, valid and test set used in
        the CreateRef.py file for even distribution of class-wise 
        data across the three stages.
    '''
    if phase == "train":
        idx_range = []
        ref = data_dict["ref"][0]
        idx2cap = {}
        j = 0
        #Abuse
        for i in range(0, 43):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Arrest
        for i in range(50, 93):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Arson
        for i in range(100, 143):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Assault
        for i in range(150, 193):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Burglary
        for i in range(200, 286):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Explosion
        for i in range(300, 343):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Fighting
        for i in range(350, 393):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Road Accidents
        for i in range(400, 529):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Robbery
        for i in range(550, 679):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Shooting
        for i in range(700, 743):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Shoplifting
        for i in range(750, 793):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Stealing
        for i in range(800, 886):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        #Vandalism
        for i in range(900, 943):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
    elif phase == "val":
        idx_range = []
        ref = data_dict['ref'][1]
        idx2cap = {}
        j = 0
        for i in range(43, 46):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(93, 96):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(143, 146):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(193, 196):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(286, 292):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(343, 346):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(393, 396):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(529, 538):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(679, 688):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(743, 746):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(793, 796):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(886, 892):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(943, 946):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
    elif phase == "test":
        idx_range = []
        ref = data_dict['ref'][2]
        idx2cap = {}
        j = 0
        for i in range(46, 50):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(96, 100):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(146, 150):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(196, 200):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(292, 300):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(346, 350):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(396, 400):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(538, 550):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(688, 700):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(746, 750):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(796, 800):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(892, 900):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
        for i in range(946, 950):
            idx_range.append(i)
            idx2cap[i] = ref[j]
            j += 1
    else:
        raise ValueError("The phase should be val or test")
    tag_feat = data_dict['tag_feat']
    res_feat = data_dict['res_feat']
    idx2gts = data_dict['idx2gts']
    for idx in idx_range:
        tag, ervid = tag_feat[idx], res_feat[idx]
        tag, ervid = np.expand_dims(tag, 0), np.expand_dims(ervid, 0)
        gts = idx2gts[idx]
        if len(gts) == 0:
            continue
        maxlen = max([len(gt) for gt in gts])
        gts_mat = np.zeros((maxlen, len(gts)), dtype=np.int32)
        for idx2, gt in enumerate(gts):
            gts_mat[:len(gt), idx2] = gt
        wanted_ops = {
            'generated_words': model.generated_words, 'test_loss': model.test_loss}
        feed_dict = {
            model.word_idx: gts_mat, model.vid_inputs: ervid, model.se_inputs: tag}
        # sel_word_idx shape: (batch_size, beam_width, n_steps)
        res = sess.run(wanted_ops, feed_dict)
        generated_words = res['generated_words']
        loss_list.append(res['test_loss'])
        for x in np.squeeze(generated_words):
            if x == 0:
                break
            sent_dict[idx].append(data_dict['idx2word'][x])
        sent_dict[idx] = [' '.join(sent_dict[idx])]
        sent_list.append(sent_dict[idx][0])
    scores = score(idx2cap, sent_dict)
    print(phase)
    pprint(scores)
    mean_loss = np.mean(loss_list)
    print('average loss:', mean_loss, flush=True)

    if "test" == phase or "train" == phase:
        with open(flags.name+'_%s_output.log'%phase, 'w') as fo:
            for sent in sent_list:
                fo.write(sent+'\n')

    return scores, mean_loss

def demo_test(sess):
    sent_dict, sent_list = defaultdict(list), []
    tag_feat = data_dict['tag_feat']
    res_feat = data_dict['res_feat']
    idx2gts = data_dict['idx2gts']
    
    for idx in range(0, tag_feat.shape[0]):
        tag, ervid = tag_feat[idx], res_feat[idx]
        tag, ervid = np.expand_dims(tag, 0), np.expand_dims(ervid, 0)
        gts = idx2gts[idx]
        if len(gts) == 0: #Only for representation purposes
           gts = [[2, 855, 1462, 1271, 1288, 583, 2, 1571, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 
                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]

        maxlen = max([len(gt) for gt in gts])
        gts_mat = np.zeros((maxlen, len(gts)), dtype=np.int32)
        for idx2, gt in enumerate(gts):
            gts_mat[:len(gt), idx2] = gt

        wanted_ops = {'generated_words': model.generated_words}
        feed_dict = {model.word_idx: gts_mat, model.vid_inputs: ervid, model.se_inputs: tag}
        res = sess.run(wanted_ops, feed_dict)
        generated_words = res['generated_words']
        for x in np.squeeze(generated_words):
            if x == 0:
                break
            sent_dict[idx].append(data_dict['idx2word'][x])
        sent_dict[idx] = [' '.join(sent_dict[idx])]
        sent_list.append(sent_dict[idx][0])
    with open("demo_test.log", 'w') as fo:
        for sent in sent_list:
            fo.write(sent+'\n')

def main():
    global data_dict, model, options
    data_dict = get_data(flags)
    options = get_options(data_dict)
    model = get_model(options)
    # model = get_gru(options)
    best_score, save_path = 0., None

    with model.graph.as_default():
        global_step = tf.compat.v1.train.get_or_create_global_step()
        train_op = get_train_op(model, options, global_step)
        saver = tf.compat.v1.train.Saver()
        config = get_config()
        sess = tf.compat.v1.Session(config=config, graph=model.graph)
        if flags.test is None:
            sess.run(tf.compat.v1.global_variables_initializer())
            train_idx1 = np.arange(options.train_size, dtype=np.int32)
            train_idx2 = np.arange(options.train_size2, dtype=np.int32)

            for idx in range(options.epoch):
                start_time = time.perf_counter()
                train_loss = []
                if idx < options.threshold:
                    np.random.shuffle(train_idx1)
                    train_part1(train_idx1, train_op, train_loss, sess, options, data_dict, model)
                else:
                    np.random.shuffle(train_idx2)
                    train_part2(train_idx2, train_op, train_loss, sess, idx, options, data_dict, model)
                mean_train_loss = np.mean(train_loss)
                print('epoch %d: loss %f' % (idx, mean_train_loss))
                scores, mean_val_loss = cal_metrics(sess, 'val')
                global METRICS, MAX, min_xe
                METRICS = {key: max(METRICS[key], scores[key]) for key in METRICS}
                for key in METRICS:
                    if METRICS[key] == 0.0:
                        METRICS[key] = 1e-18
                overall_score1 = np.mean([scores[key] / METRICS[key] for key in METRICS])
                overall_score2 = np.mean([MAX[key] / METRICS[key] for key in METRICS])
                if overall_score1 > overall_score2:
                    MAX = scores
                    save_path = saver.save(sess, './saves/%s-best.ckpt'%flags.name)
                    print('Epoch %d: the best model has been saved as %s.'% (idx, save_path), flush=True)
                end_time = time.perf_counter()
                print('%d epoch: %.2fs.' % (idx, end_time - start_time))
            saver.restore(sess, save_path)
            cal_metrics(sess, "train")
            cal_metrics(sess, 'test')
        else:
            saver.restore(sess, flags.test)
            if flags.demo == 'True':
                demo_test(sess)
            else:
                cal_metrics(sess, 'train')
                cal_metrics(sess, 'val')
                cal_metrics(sess, 'test')
        sess.close()


if __name__ == "__main__":
    tf.compat.v1.disable_v2_behavior()
    tf.compat.v1.app.flags.DEFINE_string('name', '1', 'name of model')
    tf.compat.v1.app.flags.DEFINE_string('corpus', None, 'Path to corpus file')
    tf.compat.v1.app.flags.DEFINE_string('ecores', None, 'Path to ECO-RES feature files')
    tf.compat.v1.app.flags.DEFINE_string('tag', None, 'Path to Tag feature files')
    tf.compat.v1.app.flags.DEFINE_string('ref', None, 'Path to reference files')
    tf.compat.v1.app.flags.DEFINE_string('test', None, 'Path to the saved parameters')
    tf.compat.v1.app.flags.DEFINE_string('demo', None, 'True or False: To test the model on individual samples')

    flags = tf.compat.v1.app.flags.FLAGS

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()

    print('Total time: %.2fs' % (end_time - start_time))
