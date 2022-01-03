import ctypes
import os, sys

path = os.path.join(os.path.dirname(sys.argv[0]), "src.so")
lib = ctypes.CDLL(path)
lib.greet()