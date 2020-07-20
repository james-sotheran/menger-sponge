# Project: Menger Sponge
# Author: James Sotheran
# Version: 2.0

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
        self.opacity = 0.2
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
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)
        # BOTTOM
        height = self.bottom1[2]
        x = np.linspace(self.bottom1[0], self.bottom2[0], self.steps)
        y = np.linspace(self.bottom1[1], self.bottom3[1], self.steps)
        X, Y = np.meshgrid(x, y)
        Z = np.array([np.linspace(height, height, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)

    def sides(self):
        # FRONT
        position = self.top1[1]
        x = np.linspace(self.top1[0], self.top2[0], self.steps)
        z = np.linspace(self.top1[2], self.bottom1[2], self.steps)
        X, Z = np.meshgrid(x, z)
        Y = np.array([np.linspace(position, position, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)
        # BACK
        position = self.top3[1]
        x = np.linspace(self.top3[0], self.top4[0], self.steps)
        z = np.linspace(self.top3[2], self.bottom3[2], self.steps)
        X, Z = np.meshgrid(x, z)
        Y = np.array([np.linspace(position, position, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)
        # RIGHT
        position = self.top2[0]
        y = np.linspace(self.top2[1], self.top4[1], self.steps)
        z = np.linspace(self.top2[2], self.bottom2[2], self.steps)
        Y, Z = np.meshgrid(y, z)
        X = np.array([np.linspace(position, position, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)
        # LEFT
        position = self.top1[0]
        y = np.linspace(self.top1[1], self.top3[1], self.steps)
        z = np.linspace(self.top1[2], self.bottom1[2], self.steps)
        Y, Z = np.meshgrid(y, z)
        X = np.array([np.linspace(position, position, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)



def draw(length, position, steps, thickness):
    drawing = drawCube(length, position, steps, thickness)
    drawCube.topAndBottom(drawing)
    drawCube.sides(drawing)


def removePoints(length, position, cubesInRow):
    pointsToRemove = []
    for i in range(0, 3):
        removeX = [position[0] + i*(length/cubesInRow), position[1] + length/cubesInRow, position[2] - length/cubesInRow]
        #print(removeX)
        pointsToRemove.append(removeX)
        removeY = [position[0] + length/cubesInRow, position[1] + i*(length/cubesInRow), position[2] - length/cubesInRow]
        pointsToRemove.append(removeY)
        removeZ = [position[0] + length/cubesInRow, position[1] + length/cubesInRow, position[2] - i*(length/cubesInRow)]
        pointsToRemove.append(removeZ)
    return pointsToRemove

def generatePoints(length, position, cubesInRow):
    cubePoints = []
    #print(position)
    pointsToRemove = removePoints(length, position, cubesInRow)
    #print("REMOVE")
    #print(pointsToRemove)
    for z in range(0, 3):
        for y in range(0, 3):
            for x in range(0, 3):
                point = [position[0] + x*(length/cubesInRow), position[1] + y*(length/cubesInRow), position[2] - z*(length/cubesInRow)]
                if point not in pointsToRemove:
                    #print(point)
                    cubePoints.append(point)

    #print("HERE")
#    print(cubePoints)
#    print(len(cubePoints))
    return cubePoints

def massDraw(length, position, cubesInRow):
    newLength = length/cubesInRow
    x = generatePoints(length, position, cubesInRow)
    print(x)
    for point in x:
        draw(newLength, point, 2, 0.5)
    return x

def menger():
    length = 900
    position = [0, 0, 0]
    # Initial cube
#    draw(length, position, 2, 2)
    # Split into 27
#    draw(length, position, 4, 0.5)
    # Remove centre
    iteration1 = massDraw(length, position, 3)
    iteration2 = []
    for point in iteration1:
        print(point)
        iteration2.extend(massDraw(length, point, 9))
    print("2")
    print(iteration2)
    for point in iteration2:
        iteration3 = massDraw(length, point, 27)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

menger()
#ax.view_init(0, 0)
plt.show()
#plt.savefig("menger.png")
#for angle in np.arange(0, 360, 0.75):
#    ax.view_init(0, angle)
#    plt.draw()
#    plt.pause(0.001)
