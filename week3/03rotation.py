import numpy as np
x,y = map(int, input('Enter Coordinates:').split())

theta = int(input('Enter angle in degrees: '))

coord = np.array([x, y])
rotMatrix = np.array([
    [np.cos(np.radians(theta)), -np.sin(np.radians(theta))],
    [np.sin(np.radians(theta)),  np.cos(np.radians(theta))]
])

res = np.dot(rotMatrix, coord)

print(f"Rotated coordinates: {res[0]:.2f}, {res[1]:.2f}")