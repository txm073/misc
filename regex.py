import re
import os
import sys

string = "#{os.getcwd()}\\client.exe"

def evalreplace(string):
    pattern = re.compile("\#\{[^\}]*\}")
    for match in re.finditer(pattern, string):
        stmt = string[match.span()[0] + 2:match.span()[1] - 1]
        string = string[:match.span()[0]] + eval(stmt.strip(), globals(), locals()) + string[match.span()[1]:]
    return string

if len(sys.argv) > 1:
    print(sys.argv)
    user_input = " ".join(sys.argv[1:])
else:
    user_input = input("Enter a command >>> ")

print(user_input)
split = [item[1:-1] if (item[0] in ("'", '"') and item[-1] in ("'", '"')) else item
            for item in re.findall("(?:\".*?\"|\S)+", user_input)]

print(split)