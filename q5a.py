from random import randint
import statistics
import matplotlib.pyplot as plt
import numpy as np

def V1 ():
    v1 = []
    for i in range(20):
        v1.append(randint(0, 10))
    a=statistics.mean(v1)
    b=statistics.median(v1)
    if a>b:
        return v1
    else: v1 = V1()
    return v1
def V2 ():
    v2 = []
    for i in range(20):
        v2.append(randint(0, 10))
    a=statistics.mean(v2)
    b=statistics.median(v2)
    if a<b:
        return v2
    else: v2 = V2()
    return v2


v1=V1()
v2=V2()

print("v1= ",v1)
print("Média_v1",statistics.mean(v1),'>',"Mediana_v1",statistics.median(v1))
print("v2= ",v2)
print("Média_v2",statistics.mean(v2),'<',"Mediana_v2",statistics.median(v2))


fig,ax = plt.subplots(1,2,figsize =(20,20))
ax[0].hist(v1,50, color = 'b',ec ='black')

ax[1].hist(v2,50, color = 'r',ec ='black')

plt.show()
