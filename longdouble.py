from ctypes import *

lib = cdll.LoadLibrary("./liblongdouble.dll")
fn = lib.greet
fn.argtypes = ()
fn.restype = c_void_p
fn(c_longdouble(5.0))