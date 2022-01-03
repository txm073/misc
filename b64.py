import string
import re

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

def encode(string):
    stream, output, pad = "", "", 0
    for char in string:
        stream += binary(ord(char), bits=8)
    pad = 6 - (len(stream) % 6)
    if pad != 6:
        stream += "0" * pad
    for i in range(0, len(stream), 6):
        bit = stream[i:i+6]
        output += encode_map[denary(bit, bits=6)]
    if pad != 6:
        output += "=" * (pad // 2)
    return output                     

def decode(string):
    invalid = re.search("[^A-Za-z0-9\/\+\=]", string)
    assert invalid is None, f"Invalid character: '{string[invalid.span()[0]]}'"
    stream, output = "", ""
    pad = 2 * string.count("=")
    for char in string.replace("=", ""):
        stream += binary(decode_map[char], bits=6)
    if pad:
        stream = stream[:-pad]
    for i in range(0, len(stream), 8):
        output += chr(denary(stream[i:i+8], bits=8))
    return output

b64_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
encode_map = {i: c for i, c in enumerate(b64_chars)}
decode_map = {c: i for i, c in enumerate(b64_chars)}

print(encode("Hey guys!"))
#print(encode("Hi guys!"))
