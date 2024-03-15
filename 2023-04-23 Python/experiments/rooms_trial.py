"""
very basic recursion of splitting rooms in alt directions with a doorway
displayed with glass and gold walls for testing
"""

from mcpi.minecraft import Minecraft 
from random import randint, randrange

class Building:
    NUMBER_OF_FLOORS = randint(1, 3)
    FLOOR_HEIGHT = randint(3, 5)
    MIN_AREA = randint(20, 25)

    def __init__(self, x1, x2, z1, z2, height, mc):
        self.mc = mc

        self.x1 = x1
        self.x2 = x2
        self.z1 = z1
        self.z2 = z2
        self.height = height

        # build Building
        self.build()

        self.room_data = []
        self.door_positions =[]

    def build(self):
        width = abs(self.x2 - self.x1)
        length = abs(self.z2 - self.z1)
        
        # make sure the floor is flat
        mc.setBlocks(self.x1, self.height, self.z1, self.x2, self.height + self.NUMBER_OF_FLOORS * self.FLOOR_HEIGHT, self.z2, 0)
        
        for i in range(self.NUMBER_OF_FLOORS):
            # build the floor
            mc.setBlocks(self.x1, self.height + i * self.FLOOR_HEIGHT, self.z1, self.x2, self.height + i * self.FLOOR_HEIGHT, self.z2, 20)
            # build the walls
            for h in range(self.FLOOR_HEIGHT):
                for x in range(width + 1):
                    mc.setBlock(self.x1 + x, self.height + i * self.FLOOR_HEIGHT + h, self.z1, 95)
                    mc.setBlock(self.x1 + x, self.height + i * self.FLOOR_HEIGHT + h, self.z2, 95)
                for z in range(1, length):
                    mc.setBlock(self.x1, self.height + i * self.FLOOR_HEIGHT + h, self.z1 + z, 95)
                    mc.setBlock(self.x2, self.height + i * self.FLOOR_HEIGHT + h, self.z1 + z, 95)
            self.recursive_room(self.x1, self.x2, self.z1, self.z2, self.height + i * self.FLOOR_HEIGHT, True)
    
    def recursive_room(self, x1, x2, z1, z2, floorHeight, direction):
        x, y, z = mc.player.getTilePos()
        width = abs(x2 - x1)
        length = abs(z2 - z1)

        area = width * length

        self.room_data = []

        if length > width:
            direction = 'z-axis'
        elif width > length:
            direction = 'x-axis'

        if length <= 5 or width <= 5:
            return
        
        if area < self.MIN_AREA:
            # appending room values into list
            self.room_data.append([x, y, z, length, width])
            return
        else:
            # split vertical
            if direction == 'x-axis':
                
                # split building along x axis
                split = randint(4, width - 4)
                
                # build split wall
                for h in range(self.FLOOR_HEIGHT):
                    for z in range(1, length):
                         mc.setBlock(x1 + split, floorHeight + h, z1 + z, 41)

                # add a doorway on the split wall
                door_pos = randint(1, length - 2)
                mc.setBlocks(x1 + split, floorHeight + 1, z1 + door_pos, x1 + split, floorHeight + 2, z1 + door_pos,0)


                #calling recursive function
                self.recursive_room(x1, x1 + split, z1, z2, floorHeight, direction)
                self.recursive_room(x1 + split, x2, z1, z2, floorHeight, direction)
           
            # split horizontals
            elif direction =='z-axis':
                # split building along z axis
                split = randint(4, length - 4)

                # build split wall
                for h in range(self.FLOOR_HEIGHT):
                    for x in range(1, width):
                        mc.setBlock(x1 + x, floorHeight + h, z1 + split, 41)
                
                # add a doorway on the split wall
                door_pos = randint(1, width - 2)
                mc.setBlocks(x1 + door_pos, floorHeight + 1, z1 + split, x1 + door_pos, floorHeight + 2, z1 + split, 0)

                # calling recursive function
                self.recursive_room(x1, x2, z1, z1 + split, floorHeight, direction)
                self.recursive_room(x1, x2, z1 + split, z2, floorHeight, direction)


if __name__ == "__main__":
    from mcpi.minecraft import Minecraft
    import random

    mc = Minecraft.create()

    pos = mc.player.getTilePos()

    # randHouse_x = [13, 14, 15, 16, 17, 18]
    # randHouse_z = [13, 14, 15, 16, 17, 18]

    test = Building(pos.x, pos.x + 13, pos.z, pos.z + 16, pos.y, mc)
