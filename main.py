import numpy as np
import matplotlib.pyplot as plt
import math

x0 = [-1.2, 0]
N = 2
M = int(1.65*N + 0.05*N**2)
xc = []
e = 0.05

def function(x):
   fx = (10*((x[0] - x[1])**2) + (x[0] - 1)**2)**4
   return fx

def triangle():
   a = 2
   d0 = a * ((N + 1) ** (1 / 2) + N - 1) / N * 2 ** (1 / 2)
   d1 = a * ((N + 1) ** (1 / 2) - 1) / N * 2 ** (1 / 2)

   x1 = [x0[0] + d1, x0[1] + d0]
   x2 = [x0[0] + d0, x0[1] + d1]

   setx = []
   xvector = [x0, x1, x2]
   xmin = 0
   counter = 0
   while 1:
       if a < 2:
           d0 = a * ((N + 1) ** (1 / 2) + N - 1) / N * 2 ** (1 / 2)
           d1 = a * ((N + 1) ** (1 / 2) - 1) / N * 2 ** (1 / 2)
           x1 = [xmin[0] + d1, xmin[1] + d0]
           x2 = [xmin[0] + d0, xmin[1] + d1]
           xvector = [xmin, x1, x2]
       fxlist = [function(xvector[0]), function(xvector[1]), function(xvector[2])]
       for x in xvector:
           if function(x) == max(fxlist):
               xmax = x
           elif function(x) == min(fxlist):
               xmin = x
           else:
               xmead = x
       xnew = []
       xc = []
       for i in range(len(x0)):
           xc.append((xmin[i] + xmead[i])/N)
       for i in range(len(x0)):
           xnew.append(2*xc[i] - xmax[i])
       xvector = [xmin, xmead, xnew]

       if counter % M == 0:
           setx.append(xvector)

           for x in setx:
               for y in x:
                   for z in y:
                       unique = np.unique(setx, return_counts = True)
           for s in unique[1]:
               if s > 1:
                   a = a*0.5
                   print('a: ', a)
                   break
           print('minimum x: ', xmin)
           print('function: ', function(xmin))
           print('iteration :', counter)
       print(function(xmax))
       if function(xmin) < e:
           print('minimum x: ', xmin)
           print('function: ', function(xmin))
           print('iteration: ', counter)
           break
       counter = counter + 1

   return setx

def calcS(x):
   s = (x[0][0] - x[2][0])*(x[1][1] - x[2][1])/2 - (x[0][1] - x[2][1])*(x[1][0] - x[2][0])/2
   return(abs(s))

a = 2
d0 = a * ((N + 1) ** (1 / 2) + N - 1) / N * 2 ** (1 / 2)
d1 = a * ((N + 1) ** (1 / 2) - 1) / N * 2 ** (1 / 2)

x1 = [x0[0] + d1, x0[1] + d0]
x2 = [x0[0] + d0, x0[1] + d1]
xvector = [x0, x1, x2]
print('S: ', calcS(xvector))


xvectorGraphic = np.array(triangle())
arrays = []
setx = triangle()
for i in range(len(setx)):
   arrays.append(np.array(setx[len(setx) - i - 1]))

plt.figure()
plt.scatter(arrays[len(arrays) - 1][:,0], arrays[len(arrays) - 1][:,1], s = 10, color = 'green')

for i in arrays:
   t1 = plt.Polygon(i[:3,:], color = 'black', fill=False)
   plt.gca().add_patch(t1)
plt.grid()
plt.show()
