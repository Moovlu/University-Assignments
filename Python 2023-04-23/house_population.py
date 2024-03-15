"""
Places prefabs inside of houses either randomly or through finding the best position.
Also checks that prefab does not collide with a wall or obstruct a door.
"""
import random as r
from mcpi import minecraft
import prefabs as p



def _check_sides_for_door(mc_object:minecraft, height:int, curr_pos:list[int], object_size:list[int]) -> tuple[bool]:
    """
    Ensures the given position does not have a door on any of the cardinal directions.
    """
    door = 64
    # Define valid direction variables
    x_is_valid = True
    nx_is_valid = True
    z_is_valid = True
    nz_is_valid = True

    # Check x side
    for iter_block in range(curr_pos[1], curr_pos[1] + object_size[1]):
        if mc_object.getBlock(curr_pos[0]+1, height, iter_block) == door:
            x_is_valid = False
        
        # Check opposite x side
        if mc_object.getBlock(curr_pos[0]-object_size[0], height, iter_block) == door:
            nx_is_valid = False

    # Check z side
    for iter_block in range(curr_pos[0] - object_size[0]+1, curr_pos[0]+1):
        if mc_object.getBlock(iter_block, height, curr_pos[1]-1) == door:
            z_is_valid = False

        # Check opposite z side
        if mc_object.getBlock(iter_block, height, curr_pos[1]+object_size[1]) == door:
            nz_is_valid = False

    # Return what sides are valid
    return x_is_valid, nx_is_valid, z_is_valid, nz_is_valid



def _get_best_location(mc_object:minecraft, pos_1:list[int], height:int, object_size:list[int]) -> list[int]|None:
    """
    Tries to find a valid position for the given room.
    Shifts the prefab away from obstruction if invalid.
    """
    # Set default current position
    curr_pos = pos_1
    curr_pos = [curr_pos[0] + object_size[0], curr_pos[1] - object_size[1]]

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



def _get_random_location(mc_object:minecraft, pos_1:list[int], pos_2:list[int], height:int, rand_prefab:list[int]) -> list[int]|None:
    """
    Finds a random location between position 1 and position 2
    """
    # Check prefab fits room
    if not (abs((pos_2[0] - pos_1[0])) >= rand_prefab.size[0] and abs((pos_2[1] - pos_1[1])) >= rand_prefab.size[1]):
        print(f"{rand_prefab.name} will not fit")
        return None

    # If either x or z is in the wrong order, rearrange
    if pos_1[0] < pos_2[0]:
        pos_1[0], pos_2[0] = pos_2[0], pos_1[0]
    if pos_1[1] < pos_2[1]:
        pos_1[1], pos_2[1] = pos_2[1], pos_1[1]

    # Attempts 5 times to find a valid position
    for _ in range(5):

        # randomise x position
        # print(f"Finding random x {pos_2[0] + rand_prefab.size[0] - 1, pos_1[0]}, size {rand_prefab.size[0]}")
        rand_x_pos = r.randint(pos_2[0] + rand_prefab.size[0] - 1, pos_1[0])

        # randomise z position
        # print(f"Finding random z {pos_2[1], pos_1[1] - rand_prefab.size[1] + 1}, size {rand_prefab.size[1]}")
        rand_z_pos = r.randint(pos_2[1], pos_1[1] - rand_prefab.size[1] + 1)

        # Check if prefab obstructs anything
        blocks_in_area = mc_object.getBlocks(rand_x_pos, height, rand_z_pos, rand_x_pos + rand_prefab.size[0], height, rand_z_pos + rand_prefab.size[1])
        valid_position = True
        for block in blocks_in_area:
            if block != 0:
                valid_position = False

        # Check if prefab will obstruct a door
        if valid_position:
            valid_side = _check_sides_for_door(mc_object, height, [rand_x_pos, rand_z_pos], rand_prefab.size)
            if valid_side[0] and valid_side[1] and valid_side[2] and valid_side[3]:

                # Position is valid, returns position
                return rand_x_pos, height, rand_z_pos



def populate_rooms(mc_object:minecraft, rooms:list, stairs_location:list=[1000,1000]):
    """
    Fills the given rooms with randomly placed prefabs.
    """
    for room in rooms:
        # Check if room contains stairs
        print(room[0], stairs_location[0])
        print(room[1], stairs_location[1])
        if room[0] == stairs_location[0] and room[1] == stairs_location[1]:
            print("Cannot place objects in room with stairs, skipping...")

        else:
            # Unpack variables from room
            pos_1 = room[0]
            pos_2 = room[1]
            height = room[2]

            print(f"Populating room '{room}' with prefabs...")

            # Pick 4 random prefabs and place them randomly
            for _ in range(4):
                rand_prefab = r.choice(p.prefab_list)
                rand_loc = _get_random_location(mc_object, pos_1, pos_2, height, rand_prefab)

                if rand_loc is not None:
                    rand_prefab.create(mc_object, rand_loc[0], rand_loc[1], rand_loc[2])



def place_staircase(mc_object:minecraft, rooms:list) -> list:
    """
    Tries to place a staircase prefab in one of the given rooms.
    """
    for room_check in rooms:
        # Checks if room is big enough to fit staircase
        if abs((room_check[1][0] - room_check[0][0])) >= p.stairs.size[0] and abs((room_check[1][1] - room_check[0][1])) >= p.stairs.size[1]:
            print(f"{room_check} is a valid room size")

            # Check if door will be obstructed
            best_location = _get_best_location(mc_object, room_check[0], room_check[2], p.stairs.size)

            # If the room is valid
            if best_location is not None:
                # Place stairs
                print(f"placing stairs at {best_location}")
                p.stairs.create(mc_object, best_location[0], best_location[1], best_location[2])
                stairs_location = [room_check[0], room_check[1]]

                return stairs_location



if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    # Example rooms
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
    # Place stairs and populate all rooms
    stairs_location = place_staircase(mc, ROOMS)
    populate_rooms(mc, ROOMS, stairs_location)