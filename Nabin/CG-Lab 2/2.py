import matplotlib.pyplot as plt

def draw_symmetric_points(ax, xc, yc, x, y):
    ax.plot(xc + x, yc + y, 'ko')  # Plot point in the first quadrant
    ax.plot(xc - x, yc + y, 'ko')  # Symmetric point in the second quadrant
    ax.plot(xc + x, yc - y, 'ko')  # Symmetric point in the fourth quadrant
    ax.plot(xc - x, yc - y, 'ko')  # Symmetric point in the third quadrant

def draw_ellipse(ax, xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
    p2 = (ry**2) * (x + 0.5)**2 + (rx**2) * (y - 1)**2 - (rx**2) * (ry**2)

    print("Region 1:")
    print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format("X", "Y", "p1", "p2", "2rx²yk", "2ry²xk"))
    print('-'*68)
    draw_symmetric_points(ax, xc, yc, x, y)
    print("{:<10} {:<10} {:<10.2f} {:<10.2f} {:<15.2f} {:<15.2f}".format(xc + x, yc + y, x, y, p1, p2, 2 * rx**2 * y, 2 * ry**2 * x))
    while 2 * (ry**2) * x < 2 * (rx**2) * y:
        x += 1
        if p1 < 0:
            p1 += 2 * (ry**2) * x + (ry**2)
        else:
            y -= 1
            p1 += 2 * (ry**2) * x - 2 * (rx**2) * y + (ry**2)

        draw_symmetric_points(ax, xc, yc, x, y)
        print("{:<10} {:<10} {:<10.2f} {:<10.2f} {:<15.2f} {:<15.2f}".format(xc + x, yc + y, x, y, p1, p2, 2 * rx**2 * y, 2 * ry**2 * x))

    print("\nRegion 2:")
    print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format("X", "Y", "p1", "p2", "2rx²yk", "2ry²xk"))
    print('-'*68)
    while y > 0:
        y -= 1
        if p2 > 0:
            p2 += (rx**2) * (1 - 2 * y)
        else:
            x += 1
            p2 += 2 * (ry**2) * x - 2 * (rx**2) * y - (rx**2)

        draw_symmetric_points(ax, xc, yc, x, y)
        print("{:<10} {:<10} {:<10.2f} {:<10.2f} {:<15.2f} {:<15.2f}".format(xc + x, yc + y, p1, p2, 2 * rx**2 * y, 2 * ry**2 * x))

# Example usage
xc, yc = map(int,input("Enter the two centre point : ").split(" ")) # Center of the ellipse
rx, ry =map(int,input("Enter radius for x and y : ").split(" "))  # Radii of the ellipse

fig, ax = plt.subplots()
draw_ellipse(ax, xc, yc, rx, ry)

plt.title('Midpoint Ellipse Drawing Algorithm')
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()