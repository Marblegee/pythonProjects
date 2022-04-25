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

# ## CREATING A Duplicate List Elements Remover Function
# lst = [12,12,3,44,56,99,12,3,44]
#
# def remove_dup(l):
#     unique = set(l)
#     u = list(unique)
#     u.sort()
#     return u
#
# print(lst)
# print(remove_dup(lst))


## Redefined built-in function 'type'
# print(type('String'))

# def type_dt(data):
#     dt = str(type(data))
#     if 'str' in dt:
#         print('string')
#     elif 'int' in dt:
#         print('Integer')
#     elif 'float' in dt:
#         print('Floating Point Number')
#     elif 'complex' in dt:
#         print('Complex Number')
#
# # print(type('Str'))
# type_dt(34)
# print(type(34))


## FUNCTION to smartly round decimal places in an addition operation

# def sum_r(*n):
#     sm = 0
#     d= []
#     for num in n:
#         sm += num
#         Num = str(num).split('.')
#         d.append(len(Num[1]))
#     min_d = min(d)
#     return round(sm, min_d)


# Exercising it my own way
# def sum_round(*a):
#     sum = 0
#     dec = []
#
#     for num in a:
#         sum += num
#         k = str(num).split('.')
#         dec.append(len(k[1]))
#         mdec = min(dec)
#     result = round(sum, mdec)
#     return result
#
# print(sum_round(54.231, 3.1948, 22.9, 3.14282))


### EXERCISES ###

# Str1 = 'Desserts'
# Str2 = "Live"
# Str3 = 'Pals'
# Str4 = 'God'
# Str5 = 'Raw'
#
# def str_rev(st):
#     stg = str(st).lower()
#     stg = stg[::-1]
#     stg = stg.capitalize()
#     print(st, ':', stg)
# str_rev(Str1)
# str_rev(Str2)
# str_rev(Str3)
# str_rev(Str4)
# str_rev(Str5)

# ## 2ND EXERCISE
#
# # Hint : Use dictionary
# guest_1 = 'jake'
# guest_2 = 'tamra'
# guest_3 = 'Ted'
#
# guests = {
#     'John': 'A011',
#     'Kyle': 'A009',
#     'Jake': 'BQ02',
#     'Tamra': 'A015',
#     'Josh': 'BQ13'
# }
#
#
# def get_key(rnd_name):
#     rnd_name = str(rnd_name).capitalize()
#     if rnd_name in guests.keys():
#         print('Key :', guests[rnd_name])
#     else:
#         print("Not Registered")
# get_key(guest_1)
# get_key(guest_2)
# get_key(guest_3)



#######     PYTHON CLASSES       ########

# class Coder():
#     def __init__(self, name):
#         self.Name = name
#
# cd = Coder('Jake')
# print(cd.Name)



class Coder():
    def __init__(self, name):
        self.Name = name
    def info(self):
        print(self.Name)
    def is_pythonner(self):
        if 'Python' in self.language:
            print(True)
        else:
            print(False)

cd = Coder('Jake')
cd.info()

## Adding attributes to class outside of the class

cd.language = ['Python', 'C'] # modify class identifiers or attributes in python
print(cd.language)
# cd.is_pythonner()
del(cd.language) # delete class attributes
print(cd.language)












































#
# print(sum_r(12.56, 12.848, 11.1567, 90.007))

# def checksm(val):
#     g = str(val).split(';')
#     print(g[0])
#
# checksm('ab  ; these are alphabets')

























