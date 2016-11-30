# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():

    def __init__(self, edge1, edge2, edge3):
        self.a = edge1
        self.b = edge2
        self.c = edge3

    def getSurface(self):
        surface = 2*(self.a*self.b + self.a*self.c + self.b*self.c)
        return surface

    def getVolume(self):
        volume = self.a*self.b*self.c
        return volume

cube = Cuboid(2, 2, 2)
print(cube.getSurface())
print(cube.getVolume())

"""cuboid = Cuboid(1, 2, 3)
print(cuboid.getSurface())
print(cuboid.getVolume())"""
