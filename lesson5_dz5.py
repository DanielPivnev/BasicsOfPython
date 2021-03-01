src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [src.pop(src.index(number)) for number in src if number in src]
result = [number for number in src if number not in result]

print(result)
