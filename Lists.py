names = ['John', 'Bob', 'Mosh', 'Sarah', 'Peter']
names[0] = 'Jon'
print(names[0])


# 2 is Mosh
# 2: is Mosh to Peter
# -1 is Peter

# find max number in list
numbers = [3, 8, 5, 11, 4, 2, 8]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# 2D lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
# 0 row 1 column = 2
