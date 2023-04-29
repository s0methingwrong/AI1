# 1.3
x = 5 >= 2
A = {1, 3, 7, 8}
B = {2, 4, 5, 10, 'apple'}
C = A & B
df = 'Антонова Антонина', 34, 'ж'
z = 'type'
D = [1, 'title', 2, 'content']
print(x, '|', type(x), '\n', A, '|', type(A), '\n', B, '|', type(B), '\n', C, '|', type(C), '\n', df, '|', type(df),
      '\n',
      z, '|', type(z), D, '|', type(D))

# 2.3
x = int(input())
if x < -5:
    print("x less than -5")
elif -5 <= x <= 5:
    print("x belongs to the interval from -5 inclusive to 5 inclusive")
else:
    print("x over 5")

# 3.3.1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[::-1]
print(b)

# 3.3.2
characteristics = ['height', 'weight', 'eyes colour']
for y in characteristics:
    print(y)

# 3.3.3
list_int = range(2, 15, 1)
print(list(list_int))

# 3.3.4
for i in range(105, 4, -25):
    print(i)

# 3.3.5
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = x[::2]
b = a[::-1]
j = 0
for i in range(0, 10, 2):
    x[i] = b[j]
    j += 1
print(x)

# 4.3.1
import random as r

from matplotlib import pyplot as plt

x = [r.uniform(0, 1), r.uniform(0, 1), r.uniform(0, 1), r.uniform(0, 1), r.uniform(0, 1)]
print(x)
average = 0
i = 0
for i in range(0, 5, 1):
    average += x[i]
average /= 5
a = sorted(x)
print('average value =', average)
print('median =', a[3])

if a[3] > average:
    print('the median is larger')
elif a[3] < average:
    print('the average value is greater')
else:
    print('the median and the mean are equal')

marks = ['1', '2', '3', '4', '5']
data = [x[0], x[1], x[2], x[3], x[4]]
plt.show()
plt.grid()
plt.scatter(marks, data)

# 4.3.2
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10, 1)
y = np.sqrt(1 + np.exp(np.sqrt(x)) + np.cos(x * x)) / abs(1 - (np.sin(x)) * (np.sin(x)) * (np.sin(x))) + np.log(
    abs(2 * x))
plt.plot(x, y)
plt.show()

# 4.3.3
import matplotlib.pyplot as plt
import numpy as np
from numpy import trapz

x = np.arange(0, 10, 1)
y = abs(np.cos(x * np.exp(np.cos(x) + np.log(x + 1))))
plt.plot(x, y, c="r")
plt.fill_between(x, y)
plt.show()

area = trapz(y)
print(area)

# 4.3.4
import matplotlib.pyplot as plt

# Apple
y1 = [77, 68, 64, 74, 79, 92, 105, 128, 115, 110, 120, 132]
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Microsoft
y2 = [168, 160, 157, 180, 184, 202, 205, 224, 210, 202, 215, 222]
x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Google
y3 = [71, 67, 59, 67, 71, 70, 74, 80, 74, 81, 88, 88]
x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)

plt.xlabel("Months")
plt.ylabel("Price per share")
plt.title("Company shares")
plt.show()

# 4.3.5
import numpy as np

print("Calculator")
a = int(input("Enter the 1st number "))

b = int(input("Enter the 2nd number "))

c = int(input(
    "Enter 1 for multiplication, 2 for division, 3 for addition, 4 for subtraction, 5 for exponent, 6 for sine, "
    "7 for cosine, 8 for exponentiation:\n"))

if c == 1:
    print(a * b)
elif c == 2:
    print(a / b)
elif c == 3:
    print(a + b)
elif c == 4:
    print(a - b)
elif c == 5:
    print(np.exp(a + b))
elif c == 6:
    print(np.sin(a + b))
elif c == 7:
    print(np.cos(a + b))
elif c == 8:
    print(a ^ b)
else:
    print('Error')
