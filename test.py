import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras import layers

if tf.config.list_physical_devices('GPU'):
    tf.config.set_visible_devices([], 'GPU')
    print("GPU is enabled")
if tf.config.list_physical_devices('MPS'):
    tf.config.experimental.set_memory_growth(tf.config.list_physical_devices('MPS')[0], True)
    print("MPS is enabled")

