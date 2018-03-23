def sum_symbol_codes(first, last):
    symbol_first = ord(first)
    symbol_last = ord(last)
    total_sum = 0
    for i in range(symbol_first, symbol_last + 1):
        total_sum += i
    return total_sum

print(sum_symbol_codes('x','x'))