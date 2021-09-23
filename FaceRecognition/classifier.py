from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import facenet
import os
import math
import pickle
from sklearn.svm import SVC
import tensorflow.compat.v1 as tf
from align import AlignDlib
import cv2

alignment = AlignDlib('dlib_landmark_predictor\shape_predictor_68_face_landmarks.dat')

class IdentityMetadata():
    def __init__(self, base, name, file):
        # dataset base directory
        self.base = base
        # identity name
        self.name = name
        # image file name
        self.file = file

    def __repr__(self):
        return self.image_path()

    def image_path(self):
        return os.path.join(self.base, self.name, self.file) 
    
def load_metadata(path):
    metadata = []
    for i in sorted(os.listdir(path)):
        for f in sorted(os.listdir(os.path.join(path, i))):
            # Check file extension. Allow only jpg/jpeg' files.
            ext = os.path.splitext(f)[1]
            if ext == '.jpg' or ext == '.jpeg' or ext == '.bmp' or ext == '.png':
                metadata.append(IdentityMetadata(path, i, f))
    return np.array(metadata)

def load_image(path):
    img = cv2.imread(path, 1)
    # OpenCV loads images with color channels
    # in BGR order. So we need to reverse them
    return img

def align_image(img):
    return alignment.align(182, img, alignment.getLargestFaceBoundingBox(img), 
                           landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

import os, shutil

def delete_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

class training:
    def __init__(self, datadir, modeldir, classifier_filename, Aligned):
        self.datadir = datadir
        self.modeldir = modeldir
        self.classifier_filename = classifier_filename
        self.align = Aligned

    def main_train(self):
        print(self.align == True)
        if (self.align == True):
            metadata = load_metadata(self.datadir)
            print('Start aligment: ' + str(len(metadata)))
            if (os.path.exists('./aligned_img')):
                delete_folder('./aligned_img')
            else:
                os.mkdir('./aligned_img')
            root_path = './aligned_img'
            for i, m in enumerate(metadata):
                print('Align ' + m.image_path())
                img = load_image(m.image_path())
                img = align_image(img)
                if (img is None):
                    print('Can not align: ' + m.image_path())
                    continue
                filename  = './aligned_img/' +  m.name + '/' + m.file
                if (os.path.exists(os.path.join(root_path, m.name))==False):
                    os.mkdir(os.path.join(root_path, m.name))
                print(filename)
                cv2.imwrite(filename,img)
            self.datadir = './detected_img'

        with tf.Graph().as_default():
            with tf.Session() as sess:
                img_data = facenet.get_dataset(self.datadir)
                path, label = facenet.get_image_paths_and_labels(img_data)
                print('Classes: %d' % len(img_data))
                print('Images: %d' % len(path))

                facenet.load_model(self.modeldir)
                images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
                embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
                phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
                embedding_size = embeddings.get_shape()[1]

                print('Extracting features of images for model')
                batch_size = 256
                image_size = 160 #160
                nrof_images = len(path)
                nrof_batches_per_epoch = int(math.ceil(1.0 * nrof_images / batch_size))
                emb_array = np.zeros((nrof_images, embedding_size))

                for i in range(nrof_batches_per_epoch):
                    start_index = i * batch_size
                    end_index = min((i + 1) * batch_size, nrof_images)
                    paths_batch = path[start_index:end_index]
                    images = facenet.load_data(paths_batch, False, False, image_size)
                    feed_dict = {images_placeholder: images, phase_train_placeholder: False}
                    emb_array[start_index:end_index, :] = sess.run(embeddings, feed_dict=feed_dict)

                classifier_file_name = os.path.expanduser(self.classifier_filename)

                # Training Started
                print('Training Started')
                model = SVC(kernel='linear', probability=True)
                model.fit(emb_array, label)

                class_names = [cls.name.replace('_', ' ') for cls in img_data]

                # Saving model
                with open(classifier_file_name, 'wb') as outfile:
                    pickle.dump((model, class_names), outfile)
                return classifier_file_name
