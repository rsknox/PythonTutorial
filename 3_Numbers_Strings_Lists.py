# The Python Tutorial (https://docs.python.org/3/tutorial/index.html)
# Section 3. An Informal Introduction to Python

# Strings
word = 'Python'
print('word = ', word)
print('word[0] = ', word[0] + '\n' + 'word[5] = ', word[5])
print('word[-1] = ', word[-1])
print('word[-5] = ', word[-5])
print('word[0:2] = ', word[0:2])  # characters from position 0 (included) to 2 (excluded)
print('word[2:5] =', word[2:5])  # characters from position 2 (included) to 5 (excluded)

# Lists
squares = [1, 4, 9, 16, 25]
print('squares: ', squares)
print('squares[0:3] = ', squares[0:3])
print(squares[4])
print('length of the list = ', len(squares))
squares = squares + [36, 49, 64, 81, 100]
print('squares: ', squares)
print('length of the list = ', len(squares))
squares.append(121)
print(squares)
print('length of the list = ', len(squares))

# Simple loop
a = 0
b = 1
while (a<1000):
    print(a, end=', ')
    a0 = a
    a = b
    b = a0 + b
