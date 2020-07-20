# Project: Menger Sponge
# Author: James Sotheran
# Version: 1.1

import matplotlib.pyplot as plt
import numpy as np

# Setting up environment
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

class drawCube:
    def __init__(self, length, initialPoint, steps, thickness):
        self.length = length
        self.top1 = np.array(initialPoint)
        self.top2 = np.add(self.top1, (length, 0, 0))
        self.top3 = np.add(self.top1, (0, length, 0))
        self.top4 = np.add(self.top3, (length, 0, 0))
        self.bottom1 = np.subtract(self.top1, (0, 0, length))
        self.bottom2 = np.subtract(self.top2, (0, 0, length))
        self.bottom3 = np.subtract(self. top3, (0, 0, length))
        self.bottom4 = np.subtract(self.top4, (0, 0, length))
        self.steps = steps
        self.thickness = thickness
        #print(self.top1, self.top2, self.top3, self.top4, self.bottom1, self.bottom2, self.bottom3, self.bottom4)

    def topAndBottom(self):
        #print(self.top1)
        # TOP
        height = self.top1[2]
        #print(self.top3)
        #print(self.top4)
        x = np.linspace(self.top1[0], self.top2[0], self.steps)
        y = np.linspace(self.top1[1], self.top3[1], self.steps)
        z = np.linspace(self.top1[2], self.top4[2], self.steps)
        X, Y = np.meshgrid(x, y)
        Z = np.array([np.linspace(height, height, self.steps)])
        ax.plot_wireframe(X, Y, Z, color="b", linewidth = self.thickness)
        # BOTTOM
        height = self.bottom1[2]
        x = np.linspace(self.bottom1[0], self.bottom2[0], self.steps)
        y = np.linspace(self.bottom1[1], self.bottom3[1], self.steps)
        X, Y = np.meshgrid(x, y)
        Z = np.array([np.linspace(height, height, self.steps)])
        ax.plot_wireframe(X, Y, Z, color="b", linewidth = self.thickness)

    def sides(self):
        # FRONT
        position = self.top1[1]
        x = np.linspace(self.top1[0], self.top2[0], self.steps)
        z = np.linspace(self.top1[2], self.bottom1[2], self.steps)
        X, Z = np.meshgrid(x, z)
        Y = np.array([np.linspace(position, position, self.steps)])
        ax.plot_wireframe(X, Y, Z, color="b", linewidth = self.thickness)
        # BACK
        position = self.top3[1]
        x = np.linspace(self.top3[0], self.top4[0], self.steps)
        z = np.linspace(self.top3[2], self.bottom3[2], self.steps)
        X, Z = np.meshgrid(x, z)
        Y = np.array([np.linspace(position, position, self.steps)])
        ax.plot_wireframe(X, Y, Z, color="b", linewidth = self.thickness)
        # RIGHT
        position = self.top2[0]
        y = np.linspace(self.top2[1], self.top4[1], self.steps)
        z = np.linspace(self.top2[2], self.bottom2[2], self.steps)
        Y, Z = np.meshgrid(y, z)
        X = np.array([np.linspace(position, position, self.steps)])
        ax.plot_wireframe(X, Y, Z, color="b", linewidth = self.thickness)
        # LEFT
        position = self.top1[0]
        y = np.linspace(self.top1[1], self.top3[1], self.steps)
        z = np.linspace(self.top1[2], self.bottom1[2], self.steps)
        Y, Z = np.meshgrid(y, z)
        X = np.array([np.linspace(position, position, self.steps)])
        ax.plot_wireframe(X, Y, Z, color="b", linewidth = self.thickness)



def draw(length, position, steps, thickness):
    drawing = drawCube(length, position, steps, thickness)
    drawCube.topAndBottom(drawing)
    drawCube.sides(drawing)


def remove(length, position, steps, thickness):
    # Remove middle in X directions
#    print("1")
    tempPosition = position[:]
#    print(position)
#    print(tempPosition)
    tempPosition[1] = position[1] + length/3
    tempPosition[2] = position[2] - length/3

    for i in range(0,3):
        draw(length/3, tempPosition, steps, thickness)
        tempPosition[0] = tempPosition[0] + length/3
    # Remove middle in Y direction
    tempPosition = position[:]
    tempPosition[0] = position[0] + length/3
    tempPosition[2] = position[2] - length/3
    for i in range(0,3):
        draw(length/3, tempPosition, steps, thickness)
        tempPosition[1] = tempPosition[1] + length/3

    #position = [0, 0, 0]
    # Remove middle in Z direction
    tempPosition = position[:]
    tempPosition[0] = position[0] + length/3
    tempPosition[1] = position[1] + length/3
    for i in range(0,3):
        draw(length/3, tempPosition, steps, thickness)
        tempPosition[2] = tempPosition[2] - length/3

#    print("2")
#    print(position)
#    print(tempPosition)
def massRemove(length, cubesInRow):
    cubePoints = []
    position = [0, 0, 0]
    print(position)
    for z in range(0, cubesInRow):
        for y in range(0, cubesInRow):
            for x in range(0, cubesInRow):
                cubePoints.append([position[0] + x*(length/cubesInRow), position[1] + y*(length/cubesInRow), position[2] - z*(length/cubesInRow)])
    print("HERE")
    print(cubePoints)
    print(len(cubePoints))
#    for i in range(0,len(cubePoints)):
#        print(cubePoints[i])
#        remove(length/3, cubePoints[i], 2, 0.5)
    for item in cubePoints:
        print(item)
        remove(length/cubesInRow, item, 2, 0.5)
    print(cubePoints)

def menger():
    length = 900
    position = [0, 0, 0]
    # Initial cube
    draw(length, position, 2, 2)
    # Split into 27
#    draw(length, position, 4, 0.5)
    # Remove centre
    remove(length, position, 2, 1)
    massRemove(900, 3)
#    massRemove(900, 27)
#print(X)
#ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#drawCube.fill(drawing)
menger()
plt.show()
#plt.savefig("menger.png")
#for angle in np.arange(0, 360, 0.75):
#    ax.view_init(30, angle)
#    plt.draw()
#    plt.pause(0.001)
