"""
Creates house and recursively splits it into rooms.
Fills the house with prefabs
"""
import random  as r
from mcpi import minecraft

mc = minecraft.Minecraft.create()

# Room Walls Offset.
OFFSET = 4

class House():
    """
    House Class
    """
## ========================================================================= ##
## ========================================================================= ##
    def __init__(self):
        self.room_coords = []
        self.frontdoor_pos = []
        self.house_stories = 0
        self.house_size = [[0,0,0],[0,0,0]]

    # Recursive Subdivision Algorithm - splits a house into random sized rooms. Will recurse until the dimensions of the room are less than OFFSET (4) * 2.
    def subdivide(self, pos_1, pos_2, axis, wall_block, wall_block_type, y_height, axis_rand_point):
        """
        Recursive Subdivision for each House
        """
        x_1, z_1, y_1 = pos_1
        x_2, z_2, y_2 = pos_2
        x_width = x_2 - x_1
        z_depth = z_1 - z_2

        # If axis is x and the width the of room to split on the x-axis is greater than OFFSET*2 - (4*2).
        if axis == 'x' and (((x_2 - x_1)) > OFFSET*2):
            # Chooses a random point to place down the splitting wall on the x-axis.
            x_rand_point = r.randint(4, (x_2 - x_1) - OFFSET)

            # Places the wall on the random x-axis point,.
            mc.setBlocks(x_1 + x_rand_point, y_1 , z_1 + 1, x_1 + x_rand_point, y_2 + y_height - 1, z_1 - (z_1 - z_2) - 1, wall_block, wall_block_type)

            # Random position on x-axis wall for the door
            random_door_pos = r.choice([1, 2, 3, z_depth - 1, z_depth - 2, z_depth - 3])

            # Placing the door
            if y_height == 5:
                mc.setBlock(x_1 + x_rand_point, y_1 + 1, z_1 - random_door_pos, 64, 8)
                mc.setBlock(x_1 + x_rand_point, y_1, z_1 - random_door_pos, 64, 0)
            elif y_height == 11:
                mc.setBlock(x_1 + x_rand_point, y_1 + 1, z_1 - random_door_pos, 64, 8)
                mc.setBlock(x_1 + x_rand_point, y_1, z_1 - random_door_pos, 64, 0)
                mc.setBlock(x_1 + x_rand_point, y_1 + 7, z_1 - random_door_pos, 64, 8)
                mc.setBlock(x_1 + x_rand_point, y_1 + 6, z_1 - random_door_pos, 64, 0)

            # Dimensions of Left Room of the Split (Not including walls)
            room_1_pos_1 = pos_1
            room_1_pos_2 = [x_1 + x_rand_point - 1, z_2, y_1]

            # Dimensions of Right Room of the Split (Not including walls)
            room_2_pos_1 = [x_1 + x_rand_point + 1, z_1, y_1]
            room_2_pos_2 = pos_2

            # Recalls subdivision function on both rooms after the x-split, but now splits on z-axis.
            self.subdivide(room_1_pos_1, room_1_pos_2, 'z', wall_block, wall_block_type, y_height, axis_rand_point)
            self.subdivide(room_2_pos_1, room_2_pos_2, 'z', wall_block, wall_block_type, y_height, axis_rand_point)

        # Repition of the split but on the z-axis now.
        elif axis == 'z' and (((z_1 - z_2)) > OFFSET*2):
            z_rand_point = r.randint(4, (z_1 - z_2) - 4)
            
            # Place wall on random z-axis point
            mc.setBlocks(x_1 - 1, y_1, z_2 + z_rand_point, x_2 + 1, y_2 + y_height - 1, z_2 + z_rand_point, wall_block, wall_block_type)

            random_door_pos = r.choice([1, 2, 3, x_width - 1, x_width - 2, x_width - 3])

            if y_height == 5:
                mc.setBlock(x_1 + random_door_pos, y_1 + 1, z_2 + z_rand_point, 64, 8)
                mc.setBlock(x_1 + random_door_pos, y_1, z_2 + z_rand_point, 64, 0)
            elif y_height == 11:
                mc.setBlock(x_1 + random_door_pos, y_1 + 1, z_2 + z_rand_point, 64, 8)
                mc.setBlock(x_1 + random_door_pos, y_1, z_2 + z_rand_point, 64, 0)
                mc.setBlock(x_1 + random_door_pos, y_1 + 7, z_2 + z_rand_point, 64, 8)
                mc.setBlock(x_1 + random_door_pos, y_1 + 6, z_2 + z_rand_point, 64, 0)
                

            room_1_pos_1 = pos_1
            room_1_pos_2 = [x_2, z_2 + z_rand_point + 1, y_1]

            room_2_pos_1 = [x_1, z_2 + z_rand_point - 1, y_1]
            room_2_pos_2 = pos_2

            # Recalls function on the x-axis for both rooms after the z-split.
            self.subdivide(room_1_pos_1, room_1_pos_2, 'x', wall_block, wall_block_type, y_height, z_rand_point)
            self.subdivide(room_2_pos_1, room_2_pos_2, 'x', wall_block, wall_block_type, y_height, z_rand_point)

        else:
            if y_height == 5:
                self.room_coords.append( [[x_1, z_1], [x_2, z_2], y_1])
            elif y_height == 11:
                self.room_coords.append( [[x_1, z_1], [x_2, z_2], y_1])
                self.room_coords.append( [[x_1, z_1], [x_2, z_2], y_1 + 6])
            return

## ========================================================================= ##
## ========================================================================= ##

    def randHouseDimensions(self, dimensions):
        return r.choice(dimensions)

    # ---------------------------------------------------------------------------------------------------------------------------------------- #

    def house(self, pos_1, pos_2):
        """
        House Class: (for now) just generates the house parameters
        """

        # Block Variables
        wood_planks = 5
        wood_planks_type = r.randint(0, 3)
        wood_log = 17
        wood_log_type = r.randint(0, 2)
        stoneBrick_stairs = 109
        glass = 20
        brick_block = 45
        stone_brick = 98
        wood_door = 64

        # Facing North
        x_1, z_1, y_1 = pos_1
        x_2, z_2, y_2 = pos_2

        self.house_size = [[x_1, y_1, z_1],[x_2, y_2, z_2]]


        # Re-arranging values to generate correctly
        if x_1 > x_2:
            x_1, x_2 = x_2, x_1
        
        if z_2 > z_1:
            z_1, z_2 = z_2, z_1

        print(x_1, x_2)
        print(z_1, z_2)

        # House Story Heights
        y_height = self.randHouseDimensions([5, 11])

        # Width/Depth of the x/z Dimensions
        x_width = x_2 - x_1
        z_depth = z_1 - z_2

        # ---------------------------------------------------------------------------------------------------------------------------------------- #

        if y_height == 5:
            # Cube of the House
            mc.setBlocks(x_1, y_1 - 1, z_1, x_2, y_2 + y_height, z_2, wood_planks, wood_planks_type)

            # Hollowing of the House Cube
            mc.setBlocks(x_1 + 1, y_1, z_1 - 1, x_2 - 1, y_1 + 4, z_2 + 1, 0)

            # Placing the Windows on every side
            mc.setBlocks(x_1 + 2, y_1 + 1, z_1, x_1 + x_width - 2, y_1 + 3, z_1, glass) # North Wall
            mc.setBlocks(x_1, y_1 + 1, z_1 - 2, x_1, y_1 + 3, z_1 - z_depth + 2, glass) # East Wall
            mc.setBlocks(x_1 + x_width, y_1 + 1, z_1 - 2, x_1 + x_width, y_1 + 3, z_1 - z_depth + 2, glass) # West Wall
            mc.setBlocks(x_1 + 2, y_1 + 1, z_1 - z_depth, x_1 + x_width - 2, y_1 + 3, z_1 - z_depth, glass) # South Wall

            # House Corners Aesthetics
            mc.setBlocks(x_1, y_1, z_1, x_1, y_1 + 4, z_1, wood_log, wood_log_type)
            mc.setBlocks(x_1 + x_width, y_1, z_1, x_1 + x_width, y_1 + 4, z_1, wood_log, wood_log_type)
            mc.setBlocks(x_1, y_1, z_1 - z_depth, x_1, y_1 + 4, z_1 - z_depth, wood_log, wood_log_type)
            mc.setBlocks(x_1 + x_width, y_1, z_1 - z_depth, x_1 + x_width, y_1 + 4, z_1 - z_depth, wood_log, wood_log_type)

            self.subdivide([x_1 + 1, z_1 - 1, y_1], [x_2 - 1, z_2 + 1, y_1], 'x', wood_planks, wood_planks_type, y_height, axis_rand_point = 0)

            self.house_stories = 1

        # ---------------------------------------------------------------------------------------------------------------------------------------- #
        
        elif y_height == 11:
            # Cube of the House
            mc.setBlocks(x_1, y_1 - 1, z_1, x_2, y_2 + y_height, z_2, wood_planks, wood_planks_type)

            # Hollowing out the House Cube
            mc.setBlocks(x_1 + 1, y_1, z_1 - 1, x_2 - 1, y_1 + 10, z_2 + 1, 0)

            # Placing the Windows on every side of the House
            # First Floor Windows
            mc.setBlocks(x_1 + 2, y_1 + 1, z_1, x_1 + x_width - 2, y_1 + 3, z_1, glass) # North Wall
            mc.setBlocks(x_1, y_1 + 1, z_1 - 2, x_1, y_1 + 3, z_1 - z_depth + 2, glass) # East Wall
            mc.setBlocks(x_1 + x_width, y_1 + 1, z_1 - 2, x_1 + x_width, y_1 + 3, z_1 - z_depth + 2, glass) # West Wall
            mc.setBlocks(x_1 + 2, y_1 + 1, z_1 - z_depth, x_1 + x_width - 2, y_1 + 3, z_1 - z_depth, glass) # South Wall
            # Second Floor Windows
            mc.setBlocks(x_1 + 2, y_1 + 7, z_1, x_1 + x_width - 2, y_1 + 9, z_1, glass) # North Wall
            mc.setBlocks(x_1, y_1 + 7, z_1 - 2, x_1, y_1 + 9, z_1 - z_depth + 2, glass) # East Wall
            mc.setBlocks(x_1 + x_width, y_1 + 7, z_1 - 2, x_1 + x_width, y_1 + 9, z_1 - z_depth + 2, glass) # West Wall
            mc.setBlocks(x_1 + 2, y_1 + 7, z_1 - z_depth, x_1 + x_width - 2, y_1 + 9, z_1 - z_depth, glass) # South Wall

            # House Second Story floor
            mc.setBlocks(x_1, y_1 + 5, z_1, x_2, y_1 + 5, z_2, wood_planks, wood_planks_type)

            # House Corners Blocks (Aesthetics)
            mc.setBlocks(x_1, y_1, z_1, x_1, y_1 + 10, z_1, wood_log, wood_log_type)
            mc.setBlocks(x_1 + x_width, y_1, z_1, x_1 + x_width, y_1 + 10, z_1, wood_log, wood_log_type)
            mc.setBlocks(x_1, y_1, z_1 - z_depth, x_1, y_1 + 10, z_1 - z_depth, wood_log, wood_log_type)
            mc.setBlocks(x_1 + x_width, y_1, z_1 - z_depth, x_1 + x_width, y_1 + 10, z_1 - z_depth, wood_log, wood_log_type)

            # Calls the recursive subdivision function, which generates the randomized-sized rooms on both stories of the house (if height is 11).
            self.subdivide([x_1 + 1, z_1 - 1, y_1], [x_2 - 1, z_2 + 1, y_1], 'x', wood_planks, wood_planks_type, y_height, axis_rand_point = 0)

            # Outer Story Divider Blocks
            mc.setBlocks(x_1, y_1 + 5, z_1, x_1 + x_width, y_1 + 5, z_1, wood_log, wood_log_type) # North Wall
            mc.setBlocks(x_1, y_1 + 5, z_1, x_1, y_1 + 5, z_1 - z_depth, wood_log, wood_log_type) # East Wall
            mc.setBlocks(x_1 + x_width, y_1 + 5, z_1, x_1 + x_width, y_1 + 5, z_1 - z_depth, wood_log, wood_log_type) # West Wall
            mc.setBlocks(x_1, y_1 + 5, z_1 - z_depth, x_1 + x_width, y_1 + 5, z_1 - z_depth, wood_log, wood_log_type) # South Wall

            self.house_stories = 2

        # ---------------------------------------------------------------------------------------------------------------------------------------- #

        # Setting with Roof (with Staircases)
        for i in range(int(x_width/2) + 1):
            mc.setBlocks(x_1 + i, y_1 + y_height + i, z_1, x_1 + i, y_1 + y_height + i, z_1 - z_depth, stoneBrick_stairs, 0)
            mc.setBlocks(x_1 + x_width - i, y_1 + y_height + i, z_1, x_1 + x_width - i, y_1 + y_height + i, z_1 - z_depth, stoneBrick_stairs, 1)
            # Setting the Gable (Area between the Roof)
            if (int(x_width/2) - i > 0):
                mc.setBlocks(x_1 + 1 + i, y_1 + y_height + i, z_1, x_1 + x_width - i - 1, y_1 + y_height + i, z_1, brick_block)
                mc.setBlocks(x_1 + 1 + i, y_1 + y_height + i, z_1 - z_depth, x_1 + x_width - i - 1, y_1 + y_height + i, z_1 - z_depth, brick_block)

        # Roof Base
        mc.setBlocks(x_1 + 1, y_1 + y_height, z_1, x_1 + x_width - 1, y_1 + y_height, z_1, stone_brick) # North Wall
        mc.setBlocks(x_1 + 1, y_1 + y_height, z_1 - z_depth, x_1 + x_width - 1, y_1 + y_height, z_1 - z_depth, stone_brick) # South Wall

        # Choosing a random side of the house for the exterior door, choosing a random location on that wall and then placing the door.
        door_sides = ["north", "south", "east", "west"]
        house_door_side = r.choice(door_sides)

        if house_door_side == "north":
            # Random position on the wall to set the door
            front_door_pos = r.randint(3, x_width - 3)
            # If Door Placement is placed infront of an interior wall/wooden planks, move it one spot to left on the x-axis.
            if mc.getBlock(x_1 + front_door_pos, y_1 + 2, z_1) == wood_planks:
                # Setting Door
                mc.setBlock(x_1 + front_door_pos - 1, y_1 + 1, z_1, wood_door, 8)
                mc.setBlock(x_1 + front_door_pos - 1, y_1, z_1, wood_door, 0)
                # Setting Door Frame
                mc.setBlocks(x_1 + front_door_pos - 2, y_1, z_1, x_1 + front_door_pos - 2, y_1 + 2, z_1, wood_planks, wood_planks_type)
                mc.setBlock(x_1 + front_door_pos - 1, y_1 + 2, z_1, wood_planks, wood_planks_type)
                # Setting the coordinates for the front of the door. To be used for path connecting.
                self.frontdoor_pos = [x_1 + front_door_pos, y_1, z_1 + 1]
            else:
                # Setting Door
                mc.setBlock(x_1 + front_door_pos, y_1 + 1, z_1, wood_door, 8)
                mc.setBlock(x_1 + front_door_pos, y_1, z_1, wood_door, 0)
                # Setting Door Frame
                mc.setBlocks(x_1 + front_door_pos - 1, y_1, z_1, x_1 + front_door_pos - 1, y_1 + 2, z_1, wood_planks, wood_planks_type)
                mc.setBlocks(x_1 + front_door_pos + 1, y_1, z_1, x_1 + front_door_pos + 1, y_1 + 2, z_1, wood_planks, wood_planks_type)
                mc.setBlock(x_1 + front_door_pos, y_1 + 2, z_1, wood_planks, wood_planks_type)
                self.frontdoor_pos = [x_1 + front_door_pos, y_1 - 1, z_1 + 1]
        
        elif house_door_side == "south":
            front_door_pos = r.randint(3, x_width - 3)
            if mc.getBlock(x_1 + front_door_pos, y_1 + 2, z_1 - z_depth) == wood_planks:
                mc.setBlock(x_1 + front_door_pos - 1, y_1 + 1, z_1 - z_depth, wood_door, 8)
                mc.setBlock(x_1 + front_door_pos - 1, y_1, z_1 - z_depth, wood_door, 0)
                mc.setBlocks(x_1 + front_door_pos - 2, y_1, z_1 - z_depth, x_1 + front_door_pos - 2, y_1 + 2, z_1 - z_depth, wood_planks, wood_planks_type)
                mc.setBlock(x_1 + front_door_pos - 1, y_1 + 2, z_1 - z_depth, wood_planks, wood_planks_type)
                self.frontdoor_pos = [x_1 + front_door_pos, y_1 - 1, z_1 - 1]
            else:
                mc.setBlock(x_1 + front_door_pos, y_1 + 1, z_1 - z_depth, wood_door, 8)
                mc.setBlock(x_1 + front_door_pos, y_1, z_1 - z_depth, wood_door, 0)
                mc.setBlocks(x_1 + front_door_pos - 1, y_1, z_1 - z_depth, x_1 + front_door_pos - 1, y_1 + 2, z_1 - z_depth, wood_planks, wood_planks_type)
                mc.setBlocks(x_1 + front_door_pos + 1, y_1, z_1 - z_depth, x_1 + front_door_pos + 1, y_1 + 2, z_1 - z_depth, wood_planks, wood_planks_type)
                mc.setBlock(x_1 + front_door_pos, y_1 + 2, z_1 - z_depth, wood_planks, wood_planks_type)
                self.frontdoor_pos = [x_1 + front_door_pos, y_1 - 1, z_1 - z_depth - 1]

        elif house_door_side == "east":
            print(z_depth)
            front_door_pos = r.randint(3, z_depth - 3)
            if mc.getBlock(x_1, y_1 + 2, z_1 - front_door_pos) == wood_planks:
                mc.setBlock(x_1, y_1 + 1, z_1 - front_door_pos - 1, wood_door, 8)
                mc.setBlock(x_1, y_1, z_1 - front_door_pos - 1, wood_door, 0)
                mc.setBlocks(x_1, y_1, z_1 - front_door_pos - 2, x_1, y_1 + 2, z_1 - front_door_pos - 2, wood_planks, wood_planks_type)
                mc.setBlock(x_1, y_1 + 2, z_1 - front_door_pos, wood_planks, wood_planks_type)
                self.frontdoor_pos = [x_1 - 1, y_1 - 1, z_1 - front_door_pos]
            else:
                mc.setBlock(x_1, y_1 + 1, z_1 - front_door_pos, wood_door, 8)
                mc.setBlock(x_1, y_1, z_1 - front_door_pos, wood_door, 0)
                mc.setBlocks(x_1, y_1, z_1 - front_door_pos - 1, x_1, y_1 + 2, z_1 - front_door_pos - 1, wood_planks, wood_planks_type)
                mc.setBlocks(x_1, y_1, z_1 - front_door_pos + 1, x_1, y_1 + 2, z_1 - front_door_pos + 1, wood_planks, wood_planks_type)
                mc.setBlock(x_1, y_1 + 2, z_1 - front_door_pos, wood_planks, wood_planks_type)
                self.frontdoor_pos = [x_1 - 1, y_1 - 1, z_1 - front_door_pos]

        elif house_door_side == "west":
            front_door_pos = r.randint(3, z_depth - 3)
            if mc.getBlock(x_1 + x_width, y_1 + 2, z_1 - front_door_pos) == wood_planks:
                mc.setBlock(x_1 + x_width, y_1 + 1, z_1 - front_door_pos - 1, wood_door, 8)
                mc.setBlock(x_1 + x_width, y_1, z_1 - front_door_pos - 1, wood_door, 0)
                mc.setBlocks(x_1 + x_width, y_1, z_1 - front_door_pos - 2, x_1 + x_width, y_1 + 2, z_1 - front_door_pos - 2, wood_planks, wood_planks_type)
                mc.setBlock(x_1 + x_width, y_1 + 2, z_1 - front_door_pos - 1, wood_planks, wood_planks_type)
                self.frontdoor_pos = [x_1 + x_width, y_1 - 1, z_1 - front_door_pos]
            else:
                mc.setBlock(x_1 + x_width, y_1 + 1, z_1 - front_door_pos, wood_door, 8)
                mc.setBlock(x_1 + x_width, y_1, z_1 - front_door_pos, wood_door, 0)
                mc.setBlocks(x_1 + x_width, y_1, z_1 - front_door_pos - 1, x_1 + x_width, y_1 + 2, z_1 - front_door_pos - 1, wood_planks, wood_planks_type)
                mc.setBlocks(x_1 + x_width, y_1, z_1 - front_door_pos + 1, x_1 + x_width, y_1 + 2, z_1 - front_door_pos + 1, wood_planks, wood_planks_type)
                mc.setBlock(x_1 + x_width, y_1 + 2, z_1 - front_door_pos, wood_planks, wood_planks_type)
                self.frontdoor_pos = [x_1 + x_width, y_1 - 1, z_1 - front_door_pos]
    

## ========================================================================= ##
## ========================================================================= ##

# Testing a house generation with random manually input coordinates
if __name__ == "__main__":
    mc.doCommand("time set day")
    mc.doCommand("weather clear")
    mc_house = House()

    mc_house.house([5682, 4923, 117], [5701, 4904, 117])
    # mc_house.house([4800, 4442, 70], [4819, 4423, 70])
    # Printing the coordinates of each individual room
    print(mc_house.room_coords)