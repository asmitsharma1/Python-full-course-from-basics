import matplotlib.pyplot as plt
import math
x=[1,2,3,4,5]
y=[]
z=[]
for i in x:
    y.append(i^2+i*2)
for m in y:
    z.append(math.sin(m))
plt.plot(x,y)
plt.plot(y,z)
plt.show()



    