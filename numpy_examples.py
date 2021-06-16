import numpy as np

print('B7.2.1.3 ------------------------------------------------')

my_secret = [x for x in range(1, 301, 7) if x%10 == 7 or x%10 == 1]
res = np.array([my_secret, [x/2 for x in my_secret], [x-100 for x in my_secret]])
print(res)
print()

print('B7.2.1.4 ------------------------------------------------')

res = np.ones(5)
print(res)
print()

# a2 = np.ones(5,5)

res = np.ones((5,5))
print(res)
print()

res = np.eye(5)
print(res)
print()

res = np.full((5,5), 1)
print(res)
print()

res = np.array([[1,2,3,4,5], [5,1,2,3,4], [4,5,1,2,3], [3,4,5,1,2], [2,3,4,5,1]])
print(res)
print()

print('B7.2.2.1 ------------------------------------------------')

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

rows_count, cols_count = big_secret.shape
last_col = cols_count - 1
last_col_sum = 0.0
for row in range(0, rows_count):
    last_col_sum += big_secret[row][last_col]

print(round(last_col_sum, 2))

print('B7.2.2.2 ------------------------------------------------')

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

fl = first_line[0:5]
sl = second_line[0:5]
tl = third_line[0:5]

res_arr = np.array([fl, sl, tl, sl, fl])
res = 0.0
for i in range(5):
    for j in range(5):
        if i == j:
            res += res_arr[i][j]

print(round(res, 2))

print('B7.2.2.3 ------------------------------------------------')

first_line = [x*y for x in range(2, 100, 6) for y in range(7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

fl = first_line[46:52]
sl = second_line[46:52]
tl = third_line[46:52]

res_arr = np.array([fl, sl, tl, sl, fl])
res = res_arr[0][0]
for i in range(1, 5):
    res *= res_arr[i][i]

print(res)

print('B7.2.2.4/5 ------------------------------------------------')

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

fl = first_line[46:52]
sl = second_line[46:52]
tl = third_line[46:52]

res_arr = np.array([fl, sl, tl, sl, fl])

for i in range(5):
    for j in range(5):
        if i % 2 == 1 and j % 2 == 1:
            res_arr[i][j] = 1
        if i % 2 == 0 and j % 2 == 0:
            res_arr[i][j] = -1

print(res_arr)

res = 1.0
for i in range(5):
    if i == j:
        res *= res_arr[i][i]

print(res)

print(' ------------------------------------------------')

first = [x**(1/2) for x in range(100)]
second = [x**(1/3) for x in range(100, 200)]
third = [x/y for x in range(200,300,2) for y in [3,5]]

great_secret = np.array([first, second, third]).T

print('B7.2.3.1 ------------------------------------------------')

print(great_secret.shape[1])

print('B7.2.3.2 ------------------------------------------------')

res_arr1 = great_secret[0]
res_arr2 = np.cos(res_arr1)
res_arr3 = res_arr2.sum()

print(round(res_arr3, 2))

print('B7.2.3.3 ------------------------------------------------')

res_arr1 = great_secret[great_secret > 50]
res_arr3 = res_arr1.sum()

print(res_arr3)

print('B7.2.3.5 ------------------------------------------------')

first = [x**(1/2) for x in range(100)]
second = [x**(1/3) for x in range(100, 200)]
third = [x/y for x in range(200,300,2) for y in [3,5]]

great_secret = np.array([first, second, third]).T

res_arr1 = np.sort(great_secret, axis=0)
res_arr2 = res_arr1[99]
res = res_arr2.sum()
print(round(res,2))

print('B7.3.1.1 ------------------------------------------------')

arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])