from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
from classifier import training
from data_preprocess import *

datadir = './detected_img'
modeldir = './model/20180402-114759.pb'
#modeldir = './model/20170511-185253.pb'
classifier_filename = './class/classifier.pkl'
def train():
    img_preprocess()
    print ("Training Start")
    obj=training(datadir,modeldir,classifier_filename,Aligned=False)
    get_file=obj.main_train()
    print('Saved classifier model to file "%s"' % get_file)
    print("All Done")
