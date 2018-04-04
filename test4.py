number = input('Введите пятизначное чмсло:')

def mult_odd(number):
    multiply_odd = 1
    odd_list = [int(digit) for digit in number if int(digit) % 2 != 0]
    for digit in odd_list:
        multiply_odd *= digit
    return multiply_odd

print(mult_odd(number))