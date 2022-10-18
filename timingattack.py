import time
import collections
import random
import string

database = {"txm073": "very secure password"}
chars = string.digits + string.ascii_letters + string.punctuation + " "


def timed(fn):
    def inner(*args, **kwargs):
        start = time.perf_counter_ns()
        value = fn(*args, **kwargs)
        elapsed = time.perf_counter_ns() - start
        return value, elapsed
    return inner


def repeat(iterations):
    def wrapper(fn):
        def inner(*args, **kwargs):
            results = [fn(*args, **kwargs) for i in range(iterations)]
            return results
        return inner
    return wrapper


def strcmp(str1, str2):
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
        time.sleep(1e-05)
    return True


def count_duplicates(array):
    count = {}
    for elem in array:
        try:
            count[elem] += 1
        except KeyError:
            count[elem] = 1
    return list(sorted(count.items(), key=lambda elem: elem[1], reverse=True))


@timed
def authenticate(user, pwd):
    return strcmp(database[user], pwd)


def crack_length(user, min_len=8, max_len=32, iterations=100):

    @repeat(iterations)
    def _crack_length():
        pwd_guess = "".join([random.choice(chars) for i in range(min_len)])
        lengths = []
        for i in range(min_len, max_len + 1):
            lengths.append((i, authenticate(user, pwd_guess)[1]))
            pwd_guess += random.choice(chars)
        lengths.sort(key=lambda elem: elem[1], reverse=True)
        return lengths[0][0]
    
    return count_duplicates(_crack_length())[0][0]


def crack_pwd(user, length, per_char_iterations=100):

    @repeat(per_char_iterations)
    def _guess_char(guess_string, idx):
        times = []
        for char in chars:
            guess = guess_string[:idx] + char + guess_string[idx:]
            times.append((char, authenticate(user, guess)[1]))
        times.sort(key=lambda elem: elem[1], reverse=True)
        return times[0][0]

    string = "".join([random.choice(chars) for i in range(length)])
    for i in range(1):
        print(_guess_char(string, i))

        most_likely_char = count_duplicates(_guess_char(string, i))[0][0]
        print(f"Character {i + 1} is most likely: {most_likely_char}")
        string = string[:i] + most_likely_char + string[i:]
    return string


if __name__ == "__main__":
    user = "txm073"
    # length = crack_length(user)
    # print("Most likely password length:", length)
    # pwd = crack_pwd(user, length)
    # print("Password:", pwd)
    def most_likely_password(passwords, reverse):    
        times = [(authenticate("txm073", pwd)[1], pwd) for pwd in passwords]
        print(times)

    passwords = ["t0000000000000000000", "a0000000000000000000"]
    most_likely_password(passwords, False)
    #most_likely_password(passwords, True)
