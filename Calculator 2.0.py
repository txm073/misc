import re
def check_string(calc):
    symbol_check = re.search("[\+\-\*\/][\+\-\*\/][\+\-\*\/]",calc)
    if symbol_check:
        return False
    symbol_check = re.search("[\+\*\/][\+\*\/]",calc)
    if symbol_check:
        return False
    symbol_check = re.search("[^\.0-9\+\-\*\/]",calc)
    if symbol_check:
        return False
    return True

show_steps = True
valid_string = False
while valid_string == False:
    calc = input("Enter a calculation: ")
    valid_option = False
    while valid_option == False:
        option = input("Would you like to see the steps? ").upper()
        option = option.replace(" ","")
        if option == "YES":
            show_steps = True
            valid_option = True
        elif option == "NO":
            show_steps = False
            valid_option = True
        else:
            print("That is not an option!")
    if show_steps:
        print(calc.replace(" ", ""))
    valid_string = check_string(calc)
    if valid_string == False:
        print("Syntax error: wrong symbols")
calc = re.sub("\-\-","+",calc)
calc = re.sub("([0-9]+\.?[0-9]*)\-([0-9]+\.?[0-9]*)",r"\1+-\2",calc)
ops = re.split("\-?[0-9]+\.?[0-9]*",calc)
ops = ops[1:-1]
if show_steps:
    print(ops)
nums = re.split("[\+\*\/]",calc)
if show_steps:
    print(ops)
    print(nums)
nums = [float(n) for n in nums]
if show_steps:
    print(nums)
while "*" in ops or "/" in ops:
    for count, operations in enumerate(ops):
        if operations == "*":
            del ops[count]
            break
        elif operations == "/":
            del ops[count]
            break
    first_num = nums[count]
    second_num = nums[count + 1]
    if show_steps:
        print('first num =',first_num)
        print('second num =',second_num)
    if operations == "*":
        answer = first_num * second_num
        if show_steps:
            print('answer =',answer)
    if operations == "/":
        answer = first_num / second_num
        if show_steps:
            print('answer now =',answer)
    del nums[count:count+2]
    nums.insert(count, answer)
    if show_steps:
        print('number list =',nums)
        print('operations list =',ops)
answer = str(sum(nums))+" "
answer = re.sub(".0 ","",answer)
print(f"Answer = {answer}")
