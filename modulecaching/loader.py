import shelve

s = shelve.open("data.bin")
print(s["mod"])
s.close()