src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[number] for number in range(len(src) - 1) if number != 0 and src[number] > src[number - 1]]
print(result)
