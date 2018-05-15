#matplotlib testing

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)
plt.figure(1)
plt.plot(x,y)


y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(2)
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])


plt.figure(3)
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('Sine')
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('Cosine')









plt.show()

