
def fibonacci_numbers(n):
    fibonacci_list = [1]
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        fibonacci_list.append(b)
    return fibonacci_list


print(sum(fibonacci_numbers(10)))
