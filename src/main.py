# ---------------------------------------------------------
# Tensorflow PixelRNN Implementation
# Licensed under The MIT License [see LICENSE for details]
# Written by Cheng-Bin Jin
# Email: sbkim0407@gmail.com
# ---------------------------------------------------------
import os
import tensorflow as tf
from solver import Solver

FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_string('gpu_index', '0', 'gpu index if you have multiple gpus, default: 0')
tf.flags.DEFINE_string('model', 'diagonal_bilstm', 'name of the model [pixelcnn, row_lstm, diagonal_bilstm]')
tf.flags.DEFINE_integer('batch_size', 100, 'batch sizes, default: 100')
tf.flags.DEFINE_string('dataset', 'mnist', 'dataset name from [mnist, cifar10], default: mnist')

tf.flags.DEFINE_bool('is_train', True, 'training or inference mode, default: True')
tf.flags.DEFINE_float('learning_rate', 1e-3, 'initial learning rate for RMSProp, default: 0.001')
tf.flags.DEFINE_integer('epochs', 400, 'number of epochs, default: 400')
tf.flags.DEFINE_integer('print_freq', 10, 'pring frequencey for loss, default: 100')
tf.flags.DEFINE_integer('save_freq', 5, 'model saving frequencey, default: 5')
tf.flags.DEFINE_integer('sample_batch', 4, 'sample batch size, default: 4')
tf.flags.DEFINE_string('load_model', None, 'folder of saved model that you wish to continue training '
                                           '(e.g. 20181130-0008), default: None')


def main(_):
    os.environ['CUDA_VISIBLE_DEVICES'] = FLAGS.gpu_index

    solver = Solver(FLAGS)
    if FLAGS.is_train:
        solver.train()
    if not FLAGS.is_train:
        solver.test()


if __name__ == '__main__':
    tf.app.run()
