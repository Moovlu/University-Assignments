import sys
sys.path.insert(0, 'C:/Users/Epicm/OneDrive - RMIT University/2023 Semester 1/RMIT Assignments/cosc2804-apr-23-assignment-1-team-09-cosc2804-apr23/')
import prefabs as p
from mcpi import minecraft
import random as r
mc = minecraft.Minecraft.create()

# ---------------------- Make test area ---------------------- #

GLASS = 95

def make_door(coords):
    x, y, z = coords
    mc.setBlock(x,y+1,z,64,8)
    mc.setBlock(x,y,z,64,0)

# Clear area
mc.setBlocks(-74, 69, 126, -53, 81, 147,0)
mc.doCommand("kill @e[type=minecraft:item]")

mc.setBlocks(-74, 69, 126, -53, 81, 147,GLASS,0) # Outer
mc.setBlocks(-73, 70, 127, -54, 81, 146,0) # hollow

mc.setBlocks(-73,75,127,-54,75,146,GLASS,1) # Second floor

mc.setBlocks(-66,70,127,-66,74,146,GLASS,2) # First floor walls
mc.setBlocks(-65,70,135,-54,74,135,GLASS,2) # First floor walls
mc.setBlocks(-67,70,140,-73,74,140,GLASS,2) # First floor walls
mc.setBlocks(-67,70,133,-73,74,133,GLASS,2) # First floor walls
mc.setBlocks(-61,70,146,-61,74,136,GLASS,2) # First floor walls
mc.setBlocks(-62,70,140,-65,74,140,GLASS,2) # First floor walls
mc.setBlocks(-58,70,134,-58,74,127,GLASS,2) # First floor walls
mc.setBlocks(-60,70,142,-54,74,142,GLASS,2) # First floor walls

DOOR_LOCATIONS = [
        [-74, 70, 136],
        [-66,70,138],
        [-70,70,133],
        [-70,70,140],
        [-64,70,140],
        [-61,70,138],
        [-57,70,142],
        [-60,70,135],
        [-58,70,130],
        [-53, 70, 137]
    ]
for location in DOOR_LOCATIONS:
    make_door(location)

# ---------------------- Actual code ---------------------- #

def _check_sides_for_door(mc_object, height, curr_pos, object_size):
    x_is_valid = True
    nx_is_valid = True
    z_is_valid = True
    nz_is_valid = True
    # Check x side
    print(f"x side block range: {curr_pos[1], curr_pos[1] + object_size[1]}")
    for block in range(curr_pos[1], curr_pos[1] + object_size[1]):
        mc_object.setBlock(curr_pos[0]+1, height, block, 1)
        if mc_object.getBlock(curr_pos[0]+1, height, block) == 64:
            x_is_valid = False
        
        # Check -x side
        mc_object.setBlock(curr_pos[0]-object_size[0], height, block, 1)
        if mc_object.getBlock(curr_pos[0]-object_size[0], height, block) == 64:
            nx_is_valid = False

    print(f"z side block range: {curr_pos[0] - object_size[0]+1, curr_pos[0]+1}")
    # Check z side
    for block in range(curr_pos[0] - object_size[0]+1, curr_pos[0]+1):
        mc_object.setBlock(block, height, curr_pos[1]-1, 1)
        if mc_object.getBlock(block, height, curr_pos[1]-1) == 64:
            z_is_valid = False

        # Check -z side
        mc_object.setBlock(block, height, curr_pos[1]+object_size[1], 1)
        if mc_object.getBlock(block, height, curr_pos[1]+object_size[1]) == 64:
            nz_is_valid = False

    # Return what sides are valid
    return x_is_valid, nx_is_valid, z_is_valid, nz_is_valid



def _get_best_location(mc_object:minecraft, pos_1:list[int], height:int, object_size:list[int]) -> list[int]|None:
    """
    Gets best location in the room
    """

    curr_pos = pos_1

    print(curr_pos[0], height, curr_pos[1] - 1)

    # Only repeats 4 times otherwise could get stuck in loop
    for _ in range(4):
        # Check which sides are valid
        x_is_valid, nx_is_valid, z_is_valid, nz_is_valid = _check_sides_for_door(mc_object, height, curr_pos, object_size)

        if x_is_valid and nx_is_valid and z_is_valid and nz_is_valid:
            # Place object (current position is valid)
            return [curr_pos[0],height,curr_pos[1]]

        if not x_is_valid and nx_is_valid and mc_object.getBlock(curr_pos[0] - object_size[0], height, curr_pos[1]) == 0:
            # Move 1 in the -x axis
            print("Position is invalid, moving 1 in -x")
            curr_pos = [curr_pos[0]-1, curr_pos[1]]

        elif not nx_is_valid and x_is_valid and mc_object.getBlock(curr_pos[0] + 1, height, curr_pos[1]) == 0:
            # Move 1 in the +x axis
            print("Position is invalid, moving 1 in +x")
            curr_pos = [curr_pos[0]+1, curr_pos[1]]

        elif not nz_is_valid and z_is_valid and mc_object.getBlock(curr_pos[0], height, curr_pos[1] + object_size[1]) == 0:
            # Move 1 in the +z axis
            print("Position is invalid, moving 1 in +z")
            curr_pos = [curr_pos[0], curr_pos[1]+1]

        elif not z_is_valid and nz_is_valid and mc_object.getBlock(curr_pos[0], height, curr_pos[1] - 1) == 0:
            # Move 1 in the -z axis
            print("Position is invalid, moving 1 in -z")
            curr_pos = [curr_pos[0], curr_pos[1]-1]

        else:
            print("Room is invalid, trying next room...")
            return None

    # Max iterations have been reached
    print("Max iterations reached, room is invalid, tring next room...")
    return None



def _get_random_location(mc_object:minecraft, pos_1:list[int], pos_2:list[int], height:int, object_size:list[int]) -> list[int]|None:
    # TODO: Move a bunch of code over here
    pass



def place_staircase(mc_object:minecraft, rooms:list):
    for room in rooms:
        if abs((room[1][0] - room[0][0])) >= p.stairs.size[0] and abs((room[1][1] - room[0][1])) >= p.stairs.size[1]:
            print(f"{room} is a valid room size")

            # Check if door will be obstructed
            best_location = _get_best_location(mc_object, room[0], room[2], p.stairs.size)

            # If the room not invalid
            if best_location is not None:
                # Place stairs
                print(f"placing stairs at {best_location}")
                p.stairs.create(mc, best_location[0], best_location[1], best_location[2])
                break

def populate_rooms(mc_object:minecraft, rooms:list):
    for room in rooms:
        # Unpack variables from room
        pos_1 = room[0]
        pos_2 = room[1]
        height = room[2]
        print(f"Populating room '{room}' with prefabs...")

        for prefab in range(4):
            # Pick random prefab
            rand_prefab = r.choice(p.prefab_list)

            # Check prefab fits room
            if abs((pos_2[0] - pos_1[0])) >= rand_prefab.size[0] and abs((pos_2[1] - pos_1[1])) >= rand_prefab.size[1]:

                for position in range(3):
                    # Get a random position
                    if pos_1[0] > pos_2[0]: 
                        if pos_2[0] >= 0:
                            rand_x_pos = r.randint(pos_2[0] - rand_prefab.size[0], pos_1[0])
                        else:
                            rand_x_pos = r.randint(pos_2[0] + rand_prefab.size[0], pos_1[0])
                    else:
                        if pos_2[0] >= 0:
                            rand_x_pos = r.randint(pos_1[0], pos_2[0] - rand_prefab.size[0])
                        else:
                            rand_x_pos = r.randint(pos_1[0], pos_2[0] + rand_prefab.size[0])
                    if pos_1[1] > pos_2[1]:
                        if pos_2[1] >= 0:
                            rand_z_pos = r.randint(pos_2[1] - rand_prefab.size[1], pos_1[1])
                        else:
                            rand_z_pos = r.randint(pos_2[1] + rand_prefab.size[1], pos_1[1])
                    else:
                        if pos_2[1] >= 0:
                            rand_z_pos = r.randint(pos_1[1], pos_2[1] - rand_prefab.size[1])
                        else:
                            rand_z_pos = r.randint(pos_1[1], pos_2[1] + rand_prefab.size[1])

                    # Check if prefab obstructs other prefabs
                    blocks_in_area = mc_object.getBlocks(rand_x_pos, height, rand_z_pos, rand_x_pos + rand_prefab.size[0], height, rand_z_pos + rand_prefab.size[1])
                    valid_position = True
                    for block in blocks_in_area:
                        if block != 0:
                            valid_position = False

                    # Check if prefab will obstruct a door
                    if valid_position:
                        valid_side = _check_sides_for_door(mc_object, height, [rand_x_pos, rand_z_pos], rand_prefab.size)
                        if valid_side[0] and valid_side[1] and valid_side[2] and valid_side[3]:
                            # Position is valid, places prefab
                            rand_prefab.create(mc_object, rand_x_pos, height, rand_z_pos)
            else:
                print(f"{rand_prefab.name} will not fit inside {room}")



if __name__ == "__main__":
    ROOMS = [
            [[-54,127],[-57,134], 70],
            [[-54,136],[-60,141], 70],
            [[-54,143],[-60,146], 70],
            [[-59,127],[-65,134], 70],
            [[-62,136],[-65,139], 70],
            [[-62,141],[-65,146], 70],
            [[-67,127],[-73,132], 70],
            [[-67,134],[-73,139], 70],
            [[-67,141],[-73,146], 70]
        ]
    # place_staircase(mc, ROOMS)
    # populate_rooms(mc, ROOMS)
