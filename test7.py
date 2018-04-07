
def fibonacci_numbers(n):
    a = 1
    b = 2
    for i in range(n):
        a, b = b, a + b
    return a

print(fibonacci_numbers(10))


