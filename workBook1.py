# SECTION 1

# Q1. sect, decimal

# Q2. if

# Q3. float \n 30

# Q4.
# float-> 45.05 \n
# complex -> 2+5y \n
# bool -> False \n
# string -> 'python' \n
# bytes -> b'python' \n
# integer -> 245 \n
# list -> ['Java', 'C++'] \n
# numeric string -> '176'


# SECTION 2
# # Q1.
#
# a, b = 1, 2
# a, b = b, a
# print(a, b)

# # Q2.
# num = 5
# print(num)
# num += 10
# print(num)

# # Q3.
# name_1, name_2, name_3 = 'Sam', 'Charles', 'Paul'
# print("Hello " + name_1 + "\n" + "Hello " + name_2 + "\n" + "Hello " + name_3)

# Q4.
# Legal ==> surname, encoded_var, VarString, IntVar, __int__, local_var.
# Illegal ==> $money, <mood>, 2AddedVar, str, 6int9, Amt-A/c

# Q5.
# Output: YoJohnSmith!
# Output2: 52591

# # Q6. Code is wrong, correct version below:
# name = "John is "
# age = 23
# txt = name + str(age)
# print(txt)

# SECTION 4
# Q1.
# 'It\'s Python'
# var = "'Python' is easy"
# "He said, 'Go' John"
# "'"Well who\'s is this?"

# # Q2.
# str1 = "the banana is yellow but the orange is orange"
# print(str1.title())

# # Q3.
# name = 'Jhon Smith'
# print(name.lower())
# print(name.upper())
# print(name[0])
# print(name[-2:])
# print(name[-5:])
# print(name[1:4])
# print(len(name))

# # Q4.
# print(chr(74) + chr(85) + chr(83) + chr(84) + chr(95) + chr(70) + chr(85) + chr(78))

# SECTION 5
# Q5.
# a= Python is easy
# b = PYTHON IS EASY
# c = python is not tough
# d = -1

# SECTION 6
# # Q1.
# # si = p*r*t/100
# # amt = p + si
# p, r, t = 35000, 3.5, 3
# si = p*r*t/100
# amt = p + si
# print('Amount:', amt)

# # Q2.
# a, b = 367, 255
# print(a + b)
# print(a - b)
# print(a / b)
# print(a * b)
# print(a % b)
# print(a // b)

# # Q3.
# num = 45.495567
# print(round(num, 5))

# # Q4.
# bs = 75000
# food = 0.4 * bs
# rent = 0.2* bs
# gs = bs - food - rent
# num = 45 + 125j
# print(gs, num.imag, max(123456, 123864, 123987, 123945), hex(34), pow(23,11), round(55.994521), min(987456, 987864, 987987, 987945))

# SECTION 7
# Q6.
# a.    Complex number cannot be converted into int
# b.    c is an invalid data type

# # Q7.
# num = 145
# num_ = 12
# nm_ = pow(145, 12)
# n_m = nm_ + num_
# _nm = n_m/num_
# _n_m = round(_nm, num_)
# print(_n_m)

# SECTION 8
# Q1.
# True, True, False, False

# # Q2.
# print(1 >2)
# print(True != True)
# print('hi' in 'Sam')

# # Q3.
# print(1 < 5)
# print('in' in 'ink')
# print(15 == int('15'))

# # Q4.
# a, b = 4, 5
# print(a < b)
# print(a > b)
# print(a == b)
# print(a != b)
# print(a <= b)
# print(a >= b)

# SECTION 9
# # Q1.
# lang = ['C', 'C++', 'Java', 'Python', 'Js']
# lang.append('Ruby')
# lang.remove('C')
# lang[4] = 'JavaScript'
# lang.sort()
# print(lang)

# # Q2.
# odd = [1,3,5,7,9]
# even = [2,4,6,8]
# num = [*odd, *even]
# num.append(10)
# print(len(num))
# num.sort(reverse=True)
# print(num)
# num.clear()
# print(num)

# # Q3.
# lst = list(range(1,26))
# print(lst)

# SECTION 10
# # Q1.
# tpl = (7,2)
# print(divmod(*tpl))

# # Q2.
# ls = [('mug', 10), ('ink', 7), ('gas', 45), ('phone', 220)]
#
# def sorter(ele):
#     return ele[1]
#
# ls.sort(key=sorter)
# ls.reverse()
# print(ls)

# # Q3.
# lst = [(1, 2), (3, 5), (), (12,), (11, 17), ()]
# empt_tpl = ()
# lst.remove(empt_tpl)
# lst.remove(empt_tpl)
# # del(lst[2], lst[4])
# print(lst)

# # SECTION 11
# a = {10, 20, 30, 40, 50, 60, 70}
# b = {33, 44, 51, 10, 20, 50, 30, 33}
# print(a | b)
# print(a & b)
# print(a - b)
# print(b - a)
# print(a ^ b)
# print(a >= b)
# print(a <= b)

# Q2.
# remove() deletes a specified element of a list but throws an error if the element does not exist,
# while discard does the same thing but will not throw an error if the target element does not exist in the list

# Q3.
#  <= or >=

# Q4.
# empt_set = set()

# # Q5.
# #  Slice syntax doesn't work on sets because sets are unordered lists and is not subscriptable
# sts = {2,4,6,8}
# print(sts[3])

# # Q6.
# s = {10, 2, -3, 4, 5, 88}
# print(len(s), max(s), min(s))
# print(sum(s))
# print(bool(77 in s))
# print(bool(-3 in s))

# SECTION 12
# # Q1.
# names = ['Sam', 'John', 'Peace', 'Charles', 'Edward']
# scr = [100, 78, 95, 66, 69]
# dt = {
#     names[0]: scr[0],
#     names[1]: scr[1],
#     names[2]: scr[2],
#     names[3]: scr[3],
#     names[4]: scr[4]
# }
# print(dt)

# # Q2.
# strs = ['I', 'Have', 'Victory', 'In', 'Jesus']
# dt = {
#     strs[0]: len(strs[0]),
#     strs[1]: len(strs[1]),
#     strs[2]: len(strs[2]),
#     strs[3]: len(strs[3]),
#     strs[4]: len(strs[4])
# }
# print(dt)


# Q3.
dt = {'A':65, 'B':66, 'C':67}
dt1 = {'E':68, 'F':69}

dt.update(dt1)
print(dt)
dt.update({'E': 69, 'F': 70})
print(dt)
