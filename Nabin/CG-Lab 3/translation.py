#LAB 3
#WAP to implement 2D geometric transformation a) translation b)rotation c) scaling 


import matplotlib.pyplot as plt 


x1, y1 = map(int, input("Enter the 1st coordinate : ").split(" ")) ; 
x2, y2 = map(int, input("Enter the 2nd coordinate: ").split(" ")); 
tx, ty = map(int, input("Enter the translated coordinate: ").split(" ")); 

var1 = x1 + tx
var = y1 + ty

var2 = x2 + tx
var3 = y2 + ty

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot([x1, x2], [y1, y2], label='Original Line')
plt.plot([var1, var2], [var, var3], label='Translated Line')
plt.legend()
plt.show()