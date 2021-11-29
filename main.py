import MyRandom
import numpy as np
x=[]
for i in range (0,5000):
    x.append(MyRandom.random())

print("均值：",np.mean(x))
print("方差：",np.var(x))




