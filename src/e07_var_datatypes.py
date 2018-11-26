#https://www.programiz.com/python-programming/variables-datatypes

#python numbers
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))
print("------------------------------")

#python list
a = [5,10,15,20,25,30,35,40]
print(a)

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])
print("------------------------------")

#python tuples
t = (5,'program', 1+3j)
print(t)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
# t[0] = 10
print("------------------------------")

#python strings
s = 'Hello world!'
print(s)

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
# s[5] ='d'
print("------------------------------")

#python set
a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))
print("------------------------------")

#python dictionary
d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
#print("d[2] = ", d[2])
print("------------------------------")

#Conversion between data types
print(float(5)) #5.0
print(int(10.6)) #10
print(int(-10.6)) #-10
print(float('2.5')) #2.5
print(str(25)) #'25'
print("------------------------------")

#Generates value error: Invalid literal for int()
#int('1p')

#convert one sequence to another
set([1,2,3]) #{1,2,3}
tuple({5,6,7}) #(5,6,7)
list('hello') #['h','e','l','l','o']

#conver to dictionary (each element as pair)
print(dict([[1,2],[3,4]])) #{1:2, 3:4}
print(dict([(3,26),(4,44)])) #{3:26, 4:44}
print("------------------------------")

#implicit conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))
print("------------------------------")

#addition of string and integer
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(num_int+num_str)
print("------------------------------")

#fixed adition between string and int
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))