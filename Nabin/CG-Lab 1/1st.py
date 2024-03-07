#LAB 01
# WAP that prompts the user to enter the co ordinates for points and then display them
import matplotlib.pyplot as plt
x1, y1=map(float,input("Enter the 1st coordinates : \n").split(" "))
print(f"Point 1 coordinates is :({x1},{y1})")
x2, y2=map(float,input("Enter the 2nd coordinates : \n").split(" "))
print(f"Point 1 coordinates is :({x2},{y2})")

plt.scatter([x1,x2],[y1,y2])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title("Nabin Joshi")
plt.grid(True)
plt.show()
