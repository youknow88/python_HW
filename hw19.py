import random

def diff_min_max(num_limit, lower_bound, upper_bound):
    lst = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    lower_bound = min(lst)
    upper_bound = max(lst)
    return upper_bound - lower_bound

print(diff_min_max(10, 200, 400))
