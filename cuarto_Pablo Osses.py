#PABLO OSSES
#Codigo consultado: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
import random
import matplotlib.pyplot as plt

lista=list()
for i in range(50):
    n = random.randint(100,1000)
    lista.append(n)
print(lista)
mediamovil=list()

for i in range(len(lista)-3):
    medialocal= (lista[i]+lista[i+1]+lista[i+2])/3
    mediamovil.append(medialocal)

print(mediamovil)
print(len(mediamovil))

x = list(lista)
# corresponding y axis values
y = range(0,50)
  
# plotting the points 

plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('BURSATIL')
  
# function to show the plot
plt.show()