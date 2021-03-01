def odd_num(n):
    return (i for i in range(1, n + 1, 2))


odd_num_1000 = odd_num(1000)
print(next(odd_num_1000))
print(next(odd_num_1000))
