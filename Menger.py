# Project: Menger Sponge
# Author: James Sotheran
# Version: 2.1

import matplotlib.pyplot as plt
import numpy as np

# Setting up environment
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Components to generate a cube
class drawCube:
    def __init__(self, length, initialPoint, steps, thickness):
        self.length = length # Length of side of cube
        self.top1 = np.array(initialPoint) # Front top left coord
        self.top2 = np.add(self.top1, (length, 0, 0)) # Front top right coord
        self.top3 = np.add(self.top1, (0, length, 0)) # Back top left coord
        self.top4 = np.add(self.top3, (length, 0, 0)) # Back top right coord
        self.bottom1 = np.subtract(self.top1, (0, 0, length))  # Front bottom left coord
        self.bottom2 = np.subtract(self.top2, (0, 0, length)) # Front bottom right coord
        self.bottom3 = np.subtract(self. top3, (0, 0, length)) # Back bottom left coord
        self.bottom4 = np.subtract(self.top4, (0, 0, length)) # Back bottom right coord
        self.steps = steps # How many parts each section is split into
        self.thickness = thickness # Outline thickness
        self.opacity = 0.4 # Opacity of surface (0 - 1)

    def topAndBottom(self):
        # TOP SURFACE
        height = self.top1[2] # Identifies Z coord to draw at
        x = np.linspace(self.top1[0], self.top2[0], self.steps) # Creates array from coord positions
        y = np.linspace(self.top1[1], self.top3[1], self.steps)
        z = np.linspace(self.top1[2], self.top4[2], self.steps)
        X, Y = np.meshgrid(x, y) # Combines X and Y
        Z = np.array([np.linspace(height, height, self.steps)]) # Needed to be 2D array
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity) # Draws surface
        # BOTTOM SURFACE
        height = self.bottom1[2]
        x = np.linspace(self.bottom1[0], self.bottom2[0], self.steps)
        y = np.linspace(self.bottom1[1], self.bottom3[1], self.steps)
        X, Y = np.meshgrid(x, y)
        Z = np.array([np.linspace(height, height, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)

    def sides(self):
        # FRONT SURFACE
        position = self.top1[1] # Same idea as height but on X and Y axis
        x = np.linspace(self.top1[0], self.top2[0], self.steps)
        z = np.linspace(self.top1[2], self.bottom1[2], self.steps)
        X, Z = np.meshgrid(x, z)
        Y = np.array([np.linspace(position, position, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)
        # BACK SURFACE
        position = self.top3[1]
        x = np.linspace(self.top3[0], self.top4[0], self.steps)
        z = np.linspace(self.top3[2], self.bottom3[2], self.steps)
        X, Z = np.meshgrid(x, z)
        Y = np.array([np.linspace(position, position, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)
        # RIGHT SURFACE
        position = self.top2[0]
        y = np.linspace(self.top2[1], self.top4[1], self.steps)
        z = np.linspace(self.top2[2], self.bottom2[2], self.steps)
        Y, Z = np.meshgrid(y, z)
        X = np.array([np.linspace(position, position, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)
        # LEFT SURFACE
        position = self.top1[0]
        y = np.linspace(self.top1[1], self.top3[1], self.steps)
        z = np.linspace(self.top1[2], self.bottom1[2], self.steps)
        Y, Z = np.meshgrid(y, z)
        X = np.array([np.linspace(position, position, self.steps)])
        ax.plot_surface(X, Y, Z, color="b", linewidth = self.thickness, alpha = self.opacity)


# Combines all aspects of cube into one functions
def draw(length, position, steps, thickness):
    drawing = drawCube(length, position, steps, thickness)
    drawCube.topAndBottom(drawing)
    drawCube.sides(drawing)

# Removes cross shape
def removePoints(length, position, cubesInRow): # cubesInRow lets program adjust length based on which iteration is happening
    pointsToRemove = []
    for i in range(0, 3):
        # Creating top1 X,Y,Z coords for each cube to be removed
        removeX = [position[0] + i*(length/cubesInRow), position[1] + length/cubesInRow, position[2] - length/cubesInRow]
        pointsToRemove.append(removeX)
        removeY = [position[0] + length/cubesInRow, position[1] + i*(length/cubesInRow), position[2] - length/cubesInRow]
        pointsToRemove.append(removeY)
        removeZ = [position[0] + length/cubesInRow, position[1] + length/cubesInRow, position[2] - i*(length/cubesInRow)]
        pointsToRemove.append(removeZ)
    return pointsToRemove

# Generates top1 points for menger sponge
def generatePoints(length, position, cubesInRow):
    cubePoints = []
    pointsToRemove = removePoints(length, position, cubesInRow) # Finding points which don't need to be generated
    for z in range(0, 3):
        for y in range(0, 3):
            for x in range(0, 3):
                point = [position[0] + x*(length/cubesInRow), position[1] + y*(length/cubesInRow), position[2] - z*(length/cubesInRow)]
                if point not in pointsToRemove:
                    cubePoints.append(point)

    return cubePoints

# Draws a cube at each point in generatePoints
def massDraw(length, position, cubesInRow):
    newLength = length/cubesInRow
    x = generatePoints(length, position, cubesInRow)
    print("Cube coordinates:")
    print(x)
    for point in x:
        draw(newLength, point, 2, 0.5)
    return x

def menger():
    length = 900
    position = [0, 0, 0]
    # Remove centre
    iteration1 = massDraw(length, position, 3)
    iteration2 = []
    for point in iteration1: # Does massDraw on every coord in previous iteration,
        iteration2.extend(massDraw(length, point, 9))
#    for point in iteration2: # Is very laggy...
#        iteration3 = massDraw(length, point, 27)

# Figure setup
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

menger()

plt.show()

#plt.savefig("menger.png") # Can save as image
#for angle in np.arange(0, 360, 0.75): # Rotation around cube
#    ax.view_init(0, angle)
#    plt.draw()
#    plt.pause(0.001)
