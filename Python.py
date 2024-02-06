#addition
# a = 2+2
# print(a)
#-----------------
#float
# a=17 / 3
# print(a)
#------------------
#squared
# a=5 ** 2
# print(a)
#----------------
# a='doesn\'t' 
# print(a)
#--------------------------
# a='"Yes," they said.'
# print(a)
#-------------------
# a='C:\some\name'
# print(a)
#----------------------
# a=3 * 'un' + 'ium'
# print(a)
#------------------
# a = ('Put several strings within parentheses '
#         'to have them joined together.')
# print(a)
#-------------------------------

a = 'Python'
# print(a[1])
# print(a[-1])
# print(a[0:2])
# print(a[:2])
# print(a[2:])


#--------------------------------


# x = int(input("Please enter an integer: "))
# #Please enter an integer: 42
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# -----------------------------------------------------------

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

#------------------------------


# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# print("vo",users)
# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#         print("v1",users)

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         print("v2",users)
#key,

#--------------------------------------------------------
        
# for i in range(5):
#     print(i)
#---------------------
    
# x=list(range(5, 10))
# [5, 6, 7, 8, 9]
# print(x)


# y=list(range(0, 10, 3))
# [0, 3, 6, 9]
# print(y)

# z=list(range(-10, -100, -30))
# [-10, -40, -70]
# print(z)

#--------------------------------------
# x=sum(range(4))  # 0 + 1 + 2 + 3

# print(x)
#=================================
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

#-----------------------------------------------------------------
        
# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)
        
#----------------------

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
# print(http_error(int(input("Enter Port:"))))

#---------------------------------

# x=print(int(input("status:")))
# if (x==0)|(x==2):
#     print(x)
# else:
#     print("not valid")


#---------------------------------------------------
# x = 'Python'
# y='or'

# print(x[2:4]+y)

#-------------------------------------------
# x=[1,2,3,67,7,89,4]
# for i in x:
#     i-i+10
#     print(i, end=' ')

#-----------------------------------------------


# x=['a','b','c']
# y=[1,2,3]
# q=[5,6,7]
# z=[x,y,q]
# # print(z)c26

# print(z[0][2],z[1][1],z[2][1])






   

