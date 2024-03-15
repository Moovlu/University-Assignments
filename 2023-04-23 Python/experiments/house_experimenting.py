from mcpi import minecraft, block
import random

mc = minecraft.Minecraft.create()

class House():
    # Random integer in a range
    def randomint(self, l, h):
        return random.randint(l,h)

    # Random element in a list
    def randHouseDimensions(self, dimensions):
        return random.choice(dimensions)
        
    def recursive_rooms(self,x1,y1,z1,x2,z2,axis):
        min_dimensions = 4
        if x2 < min_dimensions or z2 < min_dimensions:
            return

        house_axis = axis
        mc.postToChat("AXIS - " + str(house_axis))

        if house_axis == 'x':
            x_midpoint = int(x2 / 2)
            mc.postToChat("X MIDPOINT - " + str(x_midpoint))

            # Facing South
            far_offset = int(x2 / 2 - 4)
            close_offset = int(x2 / 2 + 4)

            x_offset = random.choice([far_offset,close_offset])

            mc.postToChat("X OFFSET - " + str(x_offset))

            mc.setBlocks(x1 + x2 - x_offset, y1, z1, x1 + x2 - x_offset, y1, z1 + z2, 42)

            if x_offset == far_offset:
                mc.postToChat("FAR")
                x1 = x1
                y1 = y1
                z1 = z1
                x2 = x2 - far_offset
                z2 = z2
                mc.postToChat(x2)
            else:
                mc.postToChat("CLOSE")
                x1 = x1 + (x2 - x_offset)
                y1 = y1
                z1 = z1
                x2 = close_offset
                z2 = z2
                mc.postToChat(x2)

            self.recursive_rooms(x1, y1, z1, x2, z2, 'z')

        elif axis == 'z':
            z_midpoint = int(z2 / 2)

            far_offset = int(z2 / 2 - 3)
            close_offset = int(z2 / 2 + 3)

            z_offset = random.choice([close_offset])

            mc.postToChat("Z OFFSET - " + str(z_offset))

            mc.setBlocks(x1, y1, z1 + z2 - z_offset, x1 + x2, y1, z1 + z2 - z_offset, 42)

            if z_offset == far_offset:
                mc.postToChat("FAR")
                x1 = x1
                y1 = y1
                z1 = z1
                x2 = x2
                z2 = z2 - far_offset

            elif z_offset == close_offset:
                mc.postToChat("CLOSE")
                mc.postToChat(close_offset)
                x1 = x1
                y1 = y1
                z1 = z1 + z2 - close_offset
                z2 = z1 + z2
                mc.postToChat(z1)
                mc.setBlock(x1,y1,z1,57)

    def house(self):
        mc.postToChat("test")

        # Player's coordinates
        x1,y1,z1 = mc.player.getPos()

        # Dimensions are odd so that the roof staircases are even
        x2 = self.randHouseDimensions([11,13,15])
        # 11 (double story house height) will be added to y2 after one story house wall recursion is complete
        y2 = self.randHouseDimensions([5]) 
        z2 = self.randHouseDimensions([11,13,15])

        # Block variables
        wood_planks = 5
        wood_planks_type = self.randomint(0,3)
        wood_log = 17
        wood_logs_type = self.randomint(0,2)
        stonebrick_stairs = 109
        glass = 20
        brick_block = 45
        wood_door = 64

        # Cube of the house
        mc.setBlocks(x1, y1-1, z1, x1+x2, y1+y2, z1+z2, wood_planks, wood_planks_type)

        # Hollowing out the cube
        mc.setBlocks(x1+1, y1, z1+1, x1+x2-1, y1+y2-1, z1+z2-1, 0)

        # Setting the Windows - Facing South
        mc.setBlocks(x1+2, y1+1, z1, x1+x2-2, y1+3, z1, glass) # front wall
        mc.setBlocks(x1, y1+1, z1+2, x1, y1+3, z1+z2-2, glass) # right wall
        mc.setBlocks(x1+x2, y1+1, z1+2, x1+x2, y1+3, z1+z2-2, glass) # left wall
        mc.setBlocks(x1+2, y1+1, z1+z2, x1+x2-2, y1+3, z1+z2, glass) # back wall

        # House Corners - Facing South
        mc.setBlocks(x1, y1, z1, x1, y1+4, z1, wood_log, wood_logs_type) # bottom right
        mc.setBlocks(x1+x2, y1, z1, x1+x2, y1+4, z1, wood_log, wood_logs_type) # bottom left
        mc.setBlocks(x1, y1, z1+z2, x1, y1+4, z1+z2, wood_log, wood_logs_type) # top right
        mc.setBlocks(x1+x2, y1, z1+z2, x1+x2, y1+4, z1+z2, wood_log, wood_logs_type) # top left

        # Setting the Roof (with Staircases)
        for i in range(int(x2/2) + 1):
            mc.setBlocks(x1+i, y1+y2+i, z1, x1+i, y1+y2+i, z1+z2, stonebrick_stairs, 0)
            mc.setBlocks(x1+x2-i, y1+y2+i, z1, x1+x2-i, y1+y2+i, z1+z2, stonebrick_stairs, 1)
            # Setting the Gable (Area between the Roof)
            if (int(x2/2) - i > 0):
                mc.setBlocks(x1+1+i, y1+y2+i, z1, x1+x2-i-1, y1+y2+i, z1, brick_block)
                mc.setBlocks(x1+1+i, y1+y2+i, z1+z2, x1+x2-i-1, y1+y2+i, z1+z2, brick_block)

        # Implementing a door on a random side of the house, and a random position on that wall (TO DO 26/04-27/04)
        door_sides = ["north", "east", "south", "west"]
        house_door_side = random.choice(door_sides)

        if house_door_side == "south":
            # Random position on the wall to set the door
            door_pos = self.randomint(2, x2-2)
            # Placing the door in wall position
            mc.setBlock(x1+x2-door_pos, y1, z1, wood_door, 0)
            mc.setBlock(x1+x2-door_pos, y1+1, z1, wood_door, 8)
        elif house_door_side == "north":
            door_pos = self.randomint(2, x2-2)
            mc.setBlock(x1+x2-door_pos, y1, z1+z2, wood_door, 0)
            mc.setBlock(x1+x2-door_pos, y1+1, z1+z2, wood_door, 8)
        elif house_door_side == "east":
            door_pos = self.randomint(2, z2-2)
            mc.setBlock(x1, y1, z1+z2-door_pos, wood_door, 0)
            mc.setBlock(x1, y1+1, z1+z2-door_pos, wood_door, 8)
        elif house_door_side == "west":
            door_pos = self.randomint(2, z2-2)
            mc.setBlock(x1+x2, y1, z1+z2-door_pos, wood_door, 0)
            mc.setBlock(x1+x2, y1+1, z1+z2-door_pos, wood_door, 8)
            

if __name__ == "__main__":
    x1,y1,z1 = mc.player.getPos()
    # Two setBlocks below are just temporary for experimenting, clears building and sets ground blocks to grass again
    mc.setBlocks(x1,y1,z1,x1+25,y1+20,z1+25,0)
    mc.setBlocks(x1,y1-1,z1,x1+25,y1-1,z1+25,2)
    # LET THERE BE LIGHTTT
    mc.doCommand("time set day")
    mc.doCommand("weather clear")

    mc_house = House()
    mc_house.house()