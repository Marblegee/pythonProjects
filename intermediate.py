# CONDITIONALS (( IF STATEMENT ))

# num1 = 1
# num2 = 2
# num3 = 0
#
# if num1== num2:
#     print('Num1 is not equal to Num2')
#     num3 = 3
# print(num3)

## Creating Conditions using or & and keywords ##
# tot = 1180
# dis = 0
# bought_sale = True
#
# if tot >= 1000 and bought_sale:
#     dis = 10
#
# total = tot - tot*dis/100
# print(tot*dis/100)
# print(total)

# elif Statements ##
# name = 'Jake'
# # age = 17
# age = 66
# status = 'Minor'
#
# if age >= 65:
#     status = 'Senior Citizen'
# elif age >= 18 and age <= 64:
#     status = 'Adult'
# print(status)

# # else STATEMENT ##
# tot = 5100
# # dis = 0
# dis = 10
# # if tot >= 5000:
# #     dis = 10
# # else:
# #     dis = 2
# if tot >= 5000:
#     pass
# else:
#     dis = 2

# total = tot - tot*dis/100
# print(tot*dis/100)
# print(total)


# # Decision CONTROL With Strings and Lists ##
# Str= 'It\'s python'
#
# if 'p' in Str:
#     Str = "It's Python"
# elif 'i' in Str:
#     Str.capitalize()
#
# print(Str)
#
# lst = ['Python', 'C', 'C++', 'Java']
# print(lst)
#
# if 'Python' not in lst:
#     lst.append('Python')
# elif 'Java' not in lst:
#     lst.append('Java')
# else:
#     lst.append('JS')
#
# print(lst)


# WHILE LOOPS ##

# i = 0
# while i != 4:
#     print('i')
#     i += 1

# num = input('>')
# print(num)
# print(type(num))

# num, i = 0, 0
# # while i < 3:
# #     num = int(input('Number_ '))
# #     sq = str(num*num)
# #     print('Square: ' + sq)
# #     i += 1
# # else:
# #     print("Done")
#
# while i < 3:
#     num = int(input('Number_ '))
#     if num == 0:
#         print('Square: 0')
#         i += 1
#         continue
#
#     if num == 1:
#         print('Program Exited!')
#         break
#     sq = str(num*num)
#     print('Square: ' + sq)
#     i += 1
# else:
#     print("Done")


####### FOR LOOPS ######
# for ele in [1,2,3]:
#     print(ele)
#
# for e in 'Python':
#     print(e)

# lst = [10, 20, 33, 45, 67]
# for num in lst:
#     print(num*2)

# lst = ['python', 'c', 'java', 12, 'JavaScript']
# for ele in lst:
#     if ele == 'JavaScript':
#         print(ele)
#         continue
#     if ele == 12:
#         break
#     print(ele.capitalize())


# lst = list(range(2,7))
# print(lst)
#
# for num in range(2, 5):
#     print(num)
#     print('Loop')


# for n in [1,2,3]:
#     for m in [1,2,3]:
#         for o in [1,2,3]:
#             print(o,n,m)
#
# # create a unique list
# # Method 1.
# lst = [1,2,5,7,8,1,3,5,8]
# lst = list(set(lst))
# print(lst)

# Method 2.
# lst = [1,2,5,7,8,1,3,5,8]
# uniques_lst = []
#
# for i in lst:
#     if i in uniques_lst:
#         continue
#     uniques_lst.append(i)
#
# uniques_lst.sort()
# print(uniques_lst)



###### SECTION 14: FUNCTIONS #########
# def product():
#     prod = 12 *25
#     print(prod)
# product()
#
# def greet(name):
#     print('Have a Nice Day!' + str(name))
# greet('Sam')
# greet('Charles')
# greet(120)

# def addition(a,b):
#     print(a + b)
# addition(9,91)
#
# def subtraction(a,b):
#     print(a-b)
# subtraction(34,11)
#
# def result(name, marks):
#     print('Name: ' + str(name))
#     print('Marks: ' + str(marks))
#
# result('Sam',97) # positional arguments
# result(marks=88, name='John') # keyword arguments

# def result(name='None', marks=None):
#     if name != 'None' or marks != None:
#         print('Name: ' + str(name))
#         print('Marks: ' + str(marks))
# result()

# ### When you don't have a definite number of expected args
# # we use a list as shown thus:
# def addition(*n):
#     sm = 0
#     for num in n:
#         sm += num
#     print(sm)
# addition(1,2,3,4,5)
# addition(41,73)


### KEYWORD ARGUMENTS
# a function taking an undefined number of key-value pairs as arguments
# def info(**kw):
#     for k,v in kw.items():
#         print(k, ': ', v)
#
# info(name='Jake',
#      age=17,
#      marks=88)
#
# info(name='Jake') # single k-v pair argument
#
# info() # empty set of argument


# ## Returning Values from User-defined functions
# def addition(*n):
#     sm = 0
#     for num in n:
#         sm+=num
#     return sm
#
# summ = addition(23,34,45)
# print(summ)


# pass keyword for functions
def Function():
    pass        # used to keep a none-operational function from returning errors

### LAMBDA Functions - usually a one-line function, used to define small functions
# sub = lambda n,m : n-m
#
# print(sub(10,4))



























