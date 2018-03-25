import random
number = random.randint(100000000000, 999999999999)
def get_max_digit(number):
    max_digit = 0
    number = str(number)
    for char in number:
        if char > max_digit:
            max_digit = char
    return max_digit
