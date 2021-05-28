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
