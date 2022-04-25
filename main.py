# SECTION 1

# print('Python')
# # This is a comment
#
# # sequence
# listTest = list[1, 3, 5, 7, 'Hello'] # elements can be changed
# testTuple = tuple(1,2,3,4,5) # elements can be changed
# testSet = {1, 3, 5, 6, 7, 8} # sets - Unique values only - cannot repeat same element or store unordered values


# VARIABLES
# var1, var2 = 'hello', 4
#
# print(var1)

#python is Case-Sensitive
#var != VAR != Var
Str = '''Master has failed more,
than the beginner has tried'''
# Master
# Master has tried
# beginner has failed
# failed
# more

# print(Str[0:6] + '\n' + Str[0:10] + ' ' + Str[-5:] + '\n' + Str[-18:-6] + ' ' + Str[11:17] + '\n' + Str[11:17] + '\n' + Str[18:22])
#
# sstt = "Z"
# print(ord(sstt))
# print(chr(88).capitalize())

# # NUMBERS IN PYTHON
# num = 20.00
# print(num, type(num))
#
# cnum = 4 +5j
# print(cnum.real, cnum.imag)
#
# num1, num2, num3 = 3, 5, (2 + 8j)
# print(num1 * num3)


# # NUMERIC FUNCTIONS
# #abs
# num1, num2, num3 = 8, 4.5, 3 +7j
# print(abs(num1))
# print(pow(num2, 2))
# print(min(num1, num2))
# print(max(num1, num2))
# print(divmod(num1, num2))
# print(round(4.238748, 2))

# # Exercise
# num1, num2, num3 = 112, 20.45, 7 +3j
# num4 = num2 * num3
# print((num1 + num2 + num3))
# print(num4)
# print(round(num1%num2, 2))
# print(round(num4.imag, 2))

# # BOOLEAN
# num1 = 5
# num2 = 4
#
# print(num1 < num2)
# print(num1 == num2)
# print(num1 >= num2)
# print(num1 <= num2)
# print(num1 != num2)
#
# a, b, c, d, e, f = 'p', 1,4.5, 9+7j, 0.0, 0+0j
# print(bool(d))
# print(bool(e))


# PYTHON LISTS
# lst1 = [1,2,3,4]
# lst2 = ['Python', 'C', 'C++']
# print(lst1 + lst2)

# # List SLICING
# lst = [1,2,3,4, 'Python', 'C', 'C++']
# print(lst[4:6])
# lst[-1] = 'Java'
# print(lst)
# sublist = lst[4:]
# print(sublist)
#
# odd = [1,3,5,7]
# evn = [0,2,4,6]
# num = [odd, evn]
# print(num)
# unpackedNum = [*odd, *evn]
# print(unpackedNum)
# #convert to set - it removed duplicate values and order the values in ascending order
# print(set(unpackedNum))

# List METHODS
odd = [1,3,5,7]
evn = [0,2,4,6]
num = [*odd, *evn]
# num.sort()
# print(num)
# num.append(8)
# print(num)
# num.remove(5)
# print(num)
# num.pop(7) # pop() takes index number as argument
# print(num)
# del(num[1])
# print(num)

# # Exercise
# print(num)
# del(num[1], num[2])
# print(num)
# num.extend([1,1])
# print(num)
#
# lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#
# del(lst[2],lst[4],lst[3])
# # lst.remove("cherry")
# # lst.remove("melon")
# # lst.remove("kiwi")
# lst.extend(["guava", "peach"])
# # lst.append("guava")
# # lst.append("peach")
# lst.reverse()
# print(lst)
# print(len(lst))


# # TUPLE - can contain heterogeneous values (strings, ints, complex numbers, etc together)
# tpl1 = (1,2,4,4,2,1)
# tpl2 = tuple("python") # saves each character as the typle elements
# print(tpl2)
# # # list can also be created using the list function
# # lst = list("python")
# # print(lst)
#
# # Accessing Tuple Elements
# print(tpl2[2])
# # tpl1[2] = 5 # element values of tuples are constant and cannot be changed or reassigned
# tp3 = tpl1 + (5,8) # you can append elements to a tuple BUT CANNOT DELETE OR CHANGE THE ELEMENTS
# # to change elements of a tuple, convert to list, change and re-convert to tuple
# lst1 = list(tpl1)
# lst1[0] = 33
# tpl1 = tuple(lst1)
# print(tpl1)
# lst1.remove(4)
# tpl1 = tuple(lst1)
# print(tpl1)
# # Embedded tuples
# TP1 = (tpl1, tpl2)
# print(TP1)
# # Unpacked Tuples
# TP2 = (*tpl1, *tpl2)
# print(TP2)
# # EXERCISE
# tp = ('python',)
# print(tp)
# print(type(tp))

# Tuple BUILT-IN FUNCTIONS
# tpl = tuple("python")
# print(tpl.index('h'))
# print(tpl.count('h'))

# tp1 = (1,8,3,6,9)
# tp1 = sorted(tp1)
# print(tp1) # it is converted to list, hence you need to use a tuple function to force it back to tuple
# tp1 = tuple(sorted(tp1))
# print(tp1)
# print(len(tp1))
# print(min(tp1), max(tp1))
#
# ttp = (12,17,11,21)
# print(sum(ttp))

# # SETS - can store unique heterogeneous values.

# sts = {1,2,3,3,3,} # sets remove repeated values and returns and ORDERED set
# sts2 = {1,4,6,3,'Python', 'Ace'}
# print(sts2)
# sts1 = set([1,2,4,2,5,6,8,3,8])
# print(sts1)
# # St = {sts, sts1} # sets cannot be embedded
# # print(St)
# ## NB: set objects are not indexed (or subscriptable)
# # st = {1, 6, 8, 0}
# # print(st[2]) # Set elements cannot be accessed because they do not have indexes. A Set is an un-ordered list

# Set FUNCTIONS
# st1, st2 = {10, 20, 30}, {90, 100}
# print(st1)
# # st1.add(50)
# # st1.remove(30)
# # st1.remove(15) # returns an error cos there is no 15, if we don't know if 15 exists, we use the discard() function
# # st1.discard(15)
# # st1.discard(10)
# st1.clear()
# st1.update(st2)
# #SETS cannot be concatenated
# # st1 = st1 + st2
# print(st1)

# # Mathematical Set Ops
#
# st1, st2 = {1, 5, 8, 9}, {1,3,6,8}
# #Union
# print(st1 | st2)
#
# #Intersection
# print(st1 & st2)
#
# # Difference
# print(st1 - st2)
#
# # Symmetric Difference
# print(st1 ^ st2)


# PYTHON DICTIONARIES
# dt = {'key':'val', 'k1':'val2'}
# print(dt)
# print(dt['k1'])

# dt = {"A":65, "B":66}
# print(dt['B'])
# print(dt.keys())
# print(dt.values())
#
# # Nested Dictionary
# dt1 = {'c':67, 'D':68 }
# Dt = {'1':dt, '2':dt1}
# print(Dt.values())
# print(Dt['2'])

# # DICTIONARY METHODS
# # create a dictionary using tuples for keys
# tp1 = ('k1', 'k2', 'k3')
# val = (4)
# dt = dict.fromkeys(tp1, val)
# print(dt)
# dt2 = dict.fromkeys(tp1)
# print(dt2)
# dt2['k1'] = 19
# dt2['k2'] = 12
# dt2['k3'] = 11
# print(dt2)
#
# dt2.pop('k2')
# print(dt2)
#
# dt2.update({'k4': 17})
# print(dt2)
#
# dt2.clear()
# print(dt2)

# EXERCISE

# tp1 = ('Set', 'VRAM', 'Slots')
# dt = dict.fromkeys(tp1)
# dt['Set'] = 'B550'
# dt['VRAM'] = '8g'
# dt['Slots'] = 4
# print(dt)

