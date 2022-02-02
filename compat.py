def calc(name1, name2):
    return (sum([ord(char) for char in name1]) * sum([ord(char) for char in name2])) % 100

print(calc("F", "F"))