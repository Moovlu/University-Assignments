"""
This experiment is to test road algorithms to get from point A to point B.
"""
from queue import PriorityQueue
from math import sqrt
from mcpi import minecraft

path_block = 208

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
        Calculates the Manhattan distance for the given coordinates
        """
        x_1, y_1, z_1 = point_1
        x_2, y_2, z_2 = self.goal

        return sqrt((x_2-x_1)**2+(z_2-z_1)**2)
    
    def _check_for_obstruction(self, point:list[int]) -> bool | None:
        # Check if path has already been there, outputs: False
        if point in self.locations:
            return False
        # Check for another path, outputs: None
        elif self.mc_object.getBlock(point[0],point[1],[point[2]]) == path_block:
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

    def _place_block(self, point:list[int]):
        """
        Checks the top block for the given location and replaces it with path or wood (if there's water)
        Does basic smoothing
        """
        pass
        

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
                best_direction = p_queue.get()
                # [0] -> distance to goal, [1] -> coordinates, [2] -> direction
                # Check validity of coordinate
                obstruction_value = self._check_for_obstruction(best_direction[1])

                if obstruction_value is None:
                    print("Merged path")
                    break
                elif obstruction_value:
                    print(f"Moving to {best_direction[1]}")
                    self.locations.append(best_direction[1])
                    px, py, pz = best_direction[1]
                    self.mc_object.setBlock(px,py,pz,path_block)
                    self._path_node(best_direction[1])
                    break


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    path_obj = Path(mc, [0,100,0], [10,100,10], [[[7,100,13],[7,100,6]],[[1000,1000,1000],[1000,1000,1000]]])
