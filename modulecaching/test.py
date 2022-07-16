import shelve
import tensorflow as tf

s = shelve.open("data.bin")
s["mod"] = tf
s.close()