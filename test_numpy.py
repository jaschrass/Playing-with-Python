# numpy testing stuff

import numpy as np

a = np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0])
a[0] = 5
print(a)

b = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(b.shape)
print(b[0,1])
print(b)

z = np.zeros((2,2))
print(z)
I = np.eye(2)
print(I)


x = np.array([[1.,2.],[3.,4.]])
y = np.array([[5.,6.],[7.,8.]])
print(x)
# elementwise math
print(x + y)
#print(np.add(x,y))
print(x - y)
#print(np.subtract(x,y)
print(x*y)
print(x/y)
print(np.sqrt(x))

# matrix multiplication
print('bla')
print(x[0,:])
print(np.dot(x[0,:],y[0,:]))
print(np.dot(x,y))

print(np.sum(x))

print(x)
x = x.T
print(x)









