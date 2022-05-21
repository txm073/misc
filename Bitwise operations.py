from math import log
import numpy as np

def get_bit_values(bit):
    place_values = [1]
    for i in range(bit-1):
        place_values.append(place_values[i] * 2)
    return place_values

def binary(n, bits=None):
    if bits is None:
        bits = int(log(n, 2)) + 1
    place_values = get_bit_values(bits)
    if n > sum(place_values):
        raise Exception(
            f"Number entered is too large to be represented in {bits} bit format"
        )
    binary = ["0"] * bits
    for index, value in enumerate(reversed(place_values)):
        if value <= n:
            n -= value 
            binary[index] = "1"
    return "".join(binary)

def denary(string, bits=8):
    place_values = get_bit_values(bits)
    denary = 0
    for char, value in zip(string, reversed(place_values)):
        if char == "1":
            denary += value
    return denary

def xor(str1, str2):
    diff = len(str1) - len(str2)
    if diff < 0:
        str1 = ("0" * diff) + str1
    elif diff > 0:
        str2 = ("0" * diff) + str2
    print(str1, str2)
    output = ""
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            output += "1"
        else:
            output += "0"
    return output

def max_int_repr(bit):
    return int(get_bit_values(bit+1)[-1]) - 1

def min_bit_repr(integer, round=True):
    if integer > max_int_repr(256):
        raise Exception(
    "Number entered is too large to be represented in binary"
                    )
    place_values = get_bit_values(256)
    if round:
        for index, value in enumerate(place_values):
            if index % 8 == 0:
                if integer < value:
                    return int(log(place_values[index-1], 2) + 1)
    else:
        for index, value in enumerate(place_values):
            if integer < value:
                return int(log(place_values[index-1], 2) + 1)
