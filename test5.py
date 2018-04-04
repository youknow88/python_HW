number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

def near_to_ten(number1, number2):
    if abs(10 - number1) > abs(10 - number2):
           return number2
    elif abs(10 - number2) > abs(10 - number1):
            return number1

print(near_to_ten(number1, number2))