# The Python Tutorial (https://docs.python.org/3/tutorial/index.html)
# Section 4. More Flow Control Tools
# ==============
# NOTE: to comment blocks of code, select lines and Ctrl /
#   to uncomment same command ctrl /
# ==============

# 4.1 If statements
# x = int(input("Please enter an integer: "))
# if (x < 0):
#     x = 0
#     print('Negative changed to zero')
# elif (x == 0):
#     print('Zero')
# elif (x == 1):
#     print('One')
# else:
#     print('Greater than one')

# 4.2 for statements
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

#4.3 The range function
#for i in range(5):
for i in range(5,10):
    print(i)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:  # % is modulus operator
            print(n, 'equals', x, '*', n//x) # // is the floor division operator;
                                             # // rounds the result down to the nearest whole number
            break
        else:
            print(n, 'is a prime number') # loop fell through without finding a factor



