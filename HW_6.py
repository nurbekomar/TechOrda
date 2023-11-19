# 1
# for i in range(1, 10):
#     print(' ' * (10 - i), '*' * i * 2)
# for i in range(1, 10):
#     print(' ' * (10 - i), '*' * i * 2)

# 2
# num = int(input())

# for i in range(1, num + 1):
#     stars = '* ' * i
#     spaces = '  ' * (2 * (num - i))
#     print(stars + spaces + stars)

# for j in range(0, num):
#     stars = '* ' * (num - j)
#     spaces = '  ' * (j * 2)
#     print(stars + spaces + stars)

# 3
array = []
for i in range(8):
    temp = []
    for j in range(8):
        if (j + i) % 2 == 0:
            temp.append('белая')
        else:
            temp.append('чёрная')
    array.append(temp)

for i in array:
    print(i)
