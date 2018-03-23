import random

def diff_even_odd(num_limit, lower_bound, upper_bound):
    sum_of_even = 0
    sum_of_odd = 0
    for i in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        if rand_num % 2 == 0:
            sum_of_even += rand_num
        if rand_num % 2 != 0:
            sum_of_odd += rand_num

        return sum_of_even - sum_of_odd

print(diff_even_odd(10, 200, 400))
