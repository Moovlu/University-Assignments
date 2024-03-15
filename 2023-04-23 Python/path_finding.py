"""
This module draws a path between the given point and the goal
"""
from queue import PriorityQueue
from math import sqrt
from mcpi import minecraft

PATH_BLOCK = 208
BRIDGE_BLOCK = 5
SCAFFOLDING_BLOCK = 5
# List of blocks that can be replaced for path
PATHABLE_LIST = [1, 2, 3, 10, 11, 12, 13, 80, 82]
# List of blocks that can be replaced for bridge
BRIDGEABLE_LIST = [8, 9, 79]


# Attempted implementation of the greedy-best-first algorithm
class Path():
    """
    Path object for drawing a line from the current position to the goal
    """

    def __init__(self, mc_object:minecraft, position:list[int], goal:list[int], house_locations:list[list]):
        self.mc_object = mc_object
        self.position = position
        self.goal = goal
        self.house_locations = house_locations
        self.locations = []
        self.previous_block = None
        self._path_node()


    def _find_distance(self, point_1:list[int]) -> float:
        """
        Calculates the Distance for the given coordinates
        """
        x_1 = point_1[0]
        z_1 = point_1[2]
        x_2 = self.goal[0]
        z_2 = self.goal[2]

        return sqrt((x_2-x_1)**2+(z_2-z_1)**2)


    def _check_for_obstruction(self, point:list[int]) -> bool | None:
        """
        Checks for any obstructions for where the block is being placed
        """
        block_height = self.mc_object.getHeight(point[0],point[2])

        # Check if path has already been there, outputs: False
        location_point = [point[0],point[2]]
        if location_point in self.locations:
            return False

        # Check for another path, outputs: None
        elif self.mc_object.getBlock(point[0], block_height, [point[2]]) == PATH_BLOCK:
            return None

        else:
            # Check for a house, outputs: False
            for house in self.house_locations:
                # Checks if block is within the x and z coordinates of a house
                # Since we don't know if x_2 or x_1 is larger, a check is done for both cases.
                if (
                        house[0][0] <= point[0] <= house[1][0] and house[0][2] <= point[2] <= house[1][2]
                        or house[0][0] <= point[0] <= house[1][0] and house[1][2] <= point[2] <= house[0][2]
                        or house[1][0] <= point[0] <= house[0][0] and house[0][2] <= point[2] <= house[1][2]
                        or house[1][0] <= point[0] <= house[0][0] and house[1][2] <= point[2] <= house[0][2]
                    ):
                    print(f"x {point} is within {house[0][0]} and {house[1][0]}")
                    return False

            # No obstructions found, outputs: True
            return True


    def _place_block(self, point:list[int]) -> list[int]:
        """
        Checks the top block for the given location and replaces it with path
        Replaces with wood if there's water, cliff or steep incline
        Removes leaves and grass
        Does basic smoothing by keeping track of previous block
        """
        # Sets block to replace with, with air
        replacing_block = 0
        x_pos = point[0]
        z_pos = point[2]

        while replacing_block == 0:
            y_height = self.mc_object.getHeight(x_pos, z_pos)
            current_block = self.mc_object.getBlock(x_pos, y_height, z_pos)

            # Check for blocks that can be removed
            if current_block in PATHABLE_LIST:
                replacing_block = PATH_BLOCK

            elif current_block in BRIDGEABLE_LIST:
                replacing_block = BRIDGE_BLOCK

            # Replace invalid block with air
            else:
                self.mc_object.setBlock(x_pos, y_height, z_pos, replacing_block)

        # If this isn't the first block, check for cliff or steep incline
        if self.previous_block is not None:

            # Check for cliff
            while (self.previous_block[1] - y_height) > 1:
                replacing_block = BRIDGE_BLOCK
                self.mc_object.setBlock(x_pos, y_height, z_pos, SCAFFOLDING_BLOCK)
                y_height += 1

            # Check for steep incline
            while (self.previous_block[1] - y_height) < -1:
                replacing_block = BRIDGE_BLOCK
                self.mc_object.setBlock(x_pos, y_height, z_pos, SCAFFOLDING_BLOCK)
                y_height -= 1

        # Place block and set previous block
        self.mc_object.setBlock(x_pos, y_height, z_pos, replacing_block)
        self.previous_block = [x_pos, y_height, z_pos]
        return [x_pos, y_height, z_pos]


    def _path_node(self, curr_pos:list[int]=None):
        """
        Finds the shortest path and moves towards it, saves location to locations
        """
        if curr_pos is None:
            curr_pos = self.position

        if curr_pos[0] == self.goal[0] and curr_pos[2] == self.goal[2]:
            print("Found goal")
        else:
            pos_x, pos_y, pos_z = curr_pos
            p_queue = PriorityQueue()

            # Check distance in x
            x_pos = [pos_x+1, pos_y, pos_z]
            x_dis = self._find_distance(x_pos)
            p_queue.put((x_dis, x_pos, "x"))

            # Check distance in -x
            nx_pos = [pos_x-1, pos_y, pos_z]
            nx_dis = self._find_distance(nx_pos)
            p_queue.put((nx_dis, nx_pos, "-x"))

            # Check distance in z
            z_pos = [pos_x, pos_y, pos_z+1]
            z_dis = self._find_distance(z_pos)
            p_queue.put((z_dis, z_pos, "z"))

            # Check distance in -z
            nz_pos = [pos_x, pos_y, pos_z-1]
            nz_dis = self._find_distance(nz_pos)
            p_queue.put((nz_dis, nz_pos, "-z"))

            # Find best direction and move towards smallest direction
            while True:
                # p_queue structure: [0] -> distance to goal, [1] -> coordinates, [2] -> direction
                best_direction = p_queue.get()
                # Check validity of coordinate
                obstruction_value = self._check_for_obstruction(best_direction[1])

                if obstruction_value is None:
                    print("Merged path")
                    break
                if obstruction_value:
                    # Get block direction and place block
                    block_direction = self._place_block(best_direction[1])
                    print(f"Moving to {block_direction}")

                    location_block_direction = [block_direction[0],block_direction[2]]
                    self.locations.append(location_block_direction)

                    self._path_node(block_direction)
                    break

# Test case
if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    test_position = [14,70,-16]
    test_goal = [-23,63,42]
    test_house_locations = [[[7,100,13],[7,100,6]],[[1000,1000,1000],[1000,1000,1000]]]
    path_obj = Path(mc, test_position, test_goal, test_house_locations)
