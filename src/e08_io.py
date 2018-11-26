#https://www.programiz.com/python-programming/input-output-import

#python output with print()
print('This sentence is output to the screen')
# Output: This sentence is output to the screen

a = 5

print('The value of a is', a)
# Output: The value of a is 5
print("----------------------------")

#print syntax:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&
print("\n----------------------------")

#Output formatting
print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread
print("----------------------------")

#python input
"""num = input('enter a number: ')
int(num)
print(num)
print("----------------------------")"""

#python imports
import math
print(math.pi)
print("----------------------------")

import sys
print(sys.path)