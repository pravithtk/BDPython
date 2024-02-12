

#if Statements
# x = int(input("Please enter an integer: "))
# # Please enter an integer: 42
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

#for Statements
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))


# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# # for user, status in users.copy().items():
# #     if status == 'inactive':
# #         del users[user]
# # print(users)



# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         print(user)

#The range() Function
        
# for i in range(5):
#     print(i)


# x=list(range(5, 10))

# print(x)


# x=list(range(0, 10, 3))
# print(x)

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

# x=range(10)
# y=range(0, 10)

# print(x)
# print(y)


#prime or not
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')


# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)


# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"
# # a = http_error(400)
# # print(a)
# b=http_error(408)
# print(b)




#------------------------------------------------------------------------
# from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")

#----------------------------------------Defining Functions

# def fib2(n):  # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = b, a+b
#     return result
# print(fib2(100))


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         reply = input(prompt)
#         if reply in {'y', 'ye', 'yes'}:
#             return True
#         if reply in {'n', 'no', 'nop', 'nope'}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# print(ask_ok(prompt))


#
# def concat(*args, sep="/"):
#     return sep.join(args)

# print(concat("earth", "mars", "venus"))


#
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# pairs
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
# print(pairs)


#
# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs

# f('spam')


#####5

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.count('apple')
# 2
# fruits.count('tangerine')
# 0
# fruits.index('banana')
# 3
# fruits.index('banana', 4)  # Find next banana starting at position 4
# 6
# fruits.reverse()
# fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# fruits.append('grape')
# fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# fruits.sort()
# fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# fruits.pop()
# 'pear'
# print(fruits)

#--------------Using Lists as Stacks¶

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# stack
# [3, 4, 5, 6, 7]
# stack.pop()
# 7
# stack
# [3, 4, 5, 6]
# stack.pop()
# 6
# stack.pop()
# 5
# stack
# [3, 4]
# print(stack)

#List Comprehensions
# squares = []
# for x in range(10):
#     squares.append(x**2)

# print(squares)


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# # The following list comprehension will transpose rows and columns:

# [[row[i] for row in matrix] for i in range(4)]

# print(matrix)

############
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[2:4]
# print(a)

# # del a[:]
# # a

# #
# t = 12345, 54321, 'hello!'
# t[0]

# print(t)

# # Tuples may be nested:
t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)
print(u)










        
        

