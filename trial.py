# this is a code letting me play with python

#edit

# Assignment and math
a = 0
b = 2
c = a + b
print(c)


# if else
a = 20
if a >= 22:
    print("if")
elif a >= 21:
    print("elif")
else:
    print("else")
	
#Function	
def someFunction(a,b):
	c = a + b
	print(c)
someFunction(a,b)

# For Loop
for i in range(1,3):
	print(i)

#While Loop	
a = 1
while a < 10:
	print(a)
	a+=1

# Strings	
myString = "b;alfkjdbxdklsjfwiojx"
print(type(myString))
num = myString.count('x')
print(num)
print(myString[2:3])

#lists
# list = [1,2,3,4]
# print(list[1])

# for i in list:
	# print(i)
	
# list.reverse()
# print(list)

#tuples
myTuple = (1,2,3)
myList = list(myTuple)
myList.append(4)
print (myList)

# dictionaries

myExample = {'something': 2, 'someElse': 20}
print(myExample['someElse'])
myExample['newItem'] = 400
for i in myExample:
	print(myExample[i])

# formatting
print('The total is %f' % 123.435)
print('The total is %.2f' % 123.435)
mstring = "a;sldjfie;wajf;efj"
print('%s' % mstring)

# try/except
var1 = '1'
try:
	var2 = var1 + 1 #wont work
except: 
	var2 = int(var1) + 1
print(var2)


# classes
class Calculator(object):
	def __init__ (self):
		self.current = 0
	def add(self, amount):
		self.current += amount
	def getCurrent(self):
		return self.current
		
	









