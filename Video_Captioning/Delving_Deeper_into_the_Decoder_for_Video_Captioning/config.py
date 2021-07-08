# -*- coding: utf-8 -*-
# Author: Adit Goyal
# Date: 2021-06-18

# configuration for UCFC-VD

class Config():
    def __init__(self, embed):
        self._n_w = 300                #Word-embedding Dimension (GloVe-840B-300d is used here)
        self._n_h = 512                #Hidden-state Dimension
        self._n_f = 64                 #Mid-input Dimension
        self._n_v = 1589               #Vocabulary Size
        self._n_t = 300                #Tagging Dimension
        self._n_z1 = 0                 #ECOnet Features Dimensions (Not used in our framework)
        self._n_z2 = 2048              #ResNeXt Features Dimensions
        self._embed = embed
        self._lr = 2e-3                #Learning Rate
        self._train_size = 817         #Number of Videos for Training (First phase of training)
        self._train_size2 = 817        #Number of Videos for Training (Second phase of training)
        self._val_size = 57            #Number of Videos for Validation
        self._test_size = 76           #Number of Videos for Testing
        self._epoch = 55               #Total Number of Epochs
        self._threshold = 32           #Number of Epochs for the First Phase
        self._max_steps = 20
        self._batch_size = 128         #Batch Size
        self._keep_prob = 0.5
        self._wd = 0.9                 #Weight Decay
        self._gamma = 0.8              #Gamma
        self._avglen = 8               #Average Length of Generated Sentences
        self._we_trainable = False

    @property
    def n_w(self):
        return self._n_w

    @property
    def n_h(self):
        return self._n_h
    
    @property
    def n_f(self):
        return self._n_f
    
    @property
    def n_v(self):
        return self._n_v
    
    @property
    def n_t(self):
        return self._n_t

    @property
    def n_z(self):
        return self._n_z2
        # return self._n_z1 + self._n_z2

    @property
    def n_z1(self):
        return self._n_z1


    @property
    def n_z2(self):
        return self._n_z2

    @property
    def embed(self):
        return self._embed

    @property
    def lr(self):
        return self._lr
    
    @property
    def train_size(self):
        return self._train_size

    @property
    def train_size2(self):
        return self._train_size2
    
    @property
    def val_size(self):
        return self._val_size
    
    @property
    def test_size(self):
        return self._test_size
    
    @property
    def epoch(self):
        return self._epoch
    
    @property
    def max_steps(self):
        return self._max_steps
     
    @property
    def threshold(self):
        return self._threshold
    
    @property
    def batch_size(self):
        return self._batch_size

    @property
    def keep_prob(self):
        return self._keep_prob
           
    @property
    def gamma(self):
        return self._gamma

    @property
    def wd(self):
        return self._wd

    @property
    def avglen(self):
        return self._avglen
   
    @property
    def we_trainable(self):
        return self._we_trainable
