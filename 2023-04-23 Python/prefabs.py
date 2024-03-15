"""
A bunch of pre-defined prefabs to when populating a house.
Prefabs will all be placed relative to the bottom left block of itself while facing +Z.
"""
from mcpi import minecraft

class Prefab():
    """
    Used to create an instance object of each prefab,
    so we can find information such as the size of each prefab.
    """
    
    def __init__(self, size:list[int], name):
        self.size = size # Size is in [x,z]
        self.name = name

    def create(self, mc_object:minecraft, x_pos, y_pos, z_pos):
        """
        Creates the item tied to the prefab object
        """
        print(f"Creating {self.name} at {x_pos,y_pos,z_pos}")
        self.PREFAB_NAMES[self.name](self, mc_object, x_pos, y_pos, z_pos)


    def _create_table(self, mc_object, x_pos, y_pos, z_pos):
        # Place fence
        mc_object.setBlock(x_pos, y_pos, z_pos, 85)
        # Place pressure plate
        mc_object.setBlock(x_pos, y_pos+1, z_pos, 72)

    def _vert_create_bookshelf(self, mc_object, x_pos, y_pos, z_pos):
        # Place bookshelves
        mc_object.setBlocks(x_pos, y_pos, z_pos, x_pos-2, y_pos+1, z_pos, 47)

    def _hor_create_bookshelf(self, mc_object, x_pos, y_pos, z_pos):
        # Place bookshelves
        mc_object.setBlocks(x_pos, y_pos, z_pos, x_pos, y_pos+1, z_pos+2, 47)

    def _create_stairs(self, mc_object, x_pos, y_pos, z_pos):
        # Clear top area
        mc_object.setBlocks(x_pos,y_pos+5,z_pos+2,x_pos-3,y_pos+5,z_pos+4,0)
        # Place stonebrick stairs
        mc_object.setBlock(x_pos,y_pos,z_pos+1,109,2)
        mc_object.setBlock(x_pos,y_pos+1,z_pos+2,109,2)
        mc_object.setBlock(x_pos,y_pos+2,z_pos+3,109,2)
        mc_object.setBlock(x_pos-1,y_pos+3,z_pos+4,109,1)
        mc_object.setBlock(x_pos-2,y_pos+4,z_pos+4,109,1)
        mc_object.setBlock(x_pos-3,y_pos+5,z_pos+3,109,3)
        # Place stonebricks
        mc_object.setBlock(x_pos,y_pos-1,z_pos,98)
        mc_object.setBlock(x_pos,y_pos,z_pos+2,98)
        mc_object.setBlock(x_pos,y_pos+1,z_pos+3,98)
        mc_object.setBlock(x_pos,y_pos+1,z_pos+3,98)
        mc_object.setBlocks(x_pos-1,y_pos+2,z_pos+4, x_pos,y_pos+2,z_pos+4,98)
        mc_object.setBlock(x_pos-3,y_pos+5,z_pos+2,98)
        mc_object.setBlock(x_pos-2,y_pos+3,z_pos+4,98)
        mc_object.setBlocks(x_pos-3,y_pos+4,z_pos+4,x_pos-3,y_pos+4,z_pos+3,98)

    def _create_lamp(self, mc_object, x_pos, y_pos, z_pos):
        mc_object.setBlock(x_pos,y_pos,z_pos, 139)
        mc_object.setBlock(x_pos,y_pos+1,z_pos, 89)
        mc_object.setBlock(x_pos,y_pos+2,z_pos, 171, 8)

    def _create_plant(self, mc_object, x_pos, y_pos, z_pos):
        mc_object.setBlock(x_pos,y_pos,z_pos, 17)
        mc_object.setBlocks(x_pos,y_pos+1,z_pos, x_pos, y_pos+2, z_pos, 18)

    def _create_village_center(self, mc_object, x_pos, y_pos, z_pos):
        # Clearing out area
        mc_object.setBlocks(x_pos + 2, y_pos - 1, z_pos - 2, x_pos - 5, y_pos + 5, z_pos + 5, 0)
        # Floor
        mc_object.setBlocks(x_pos + 2, y_pos - 1, z_pos - 2, x_pos - 5, y_pos - 1, z_pos + 5, 208)
        # Bottom Left Corner
        mc_object.setBlock(x_pos + 1, y_pos - 1, z_pos - 1, 4)
        mc_object.setBlocks(x_pos + 1, y_pos, z_pos - 1, x_pos + 1, y_pos + 4, z_pos - 1, 85)
        # Bottom Right Corner
        mc_object.setBlock(x_pos - 4, y_pos - 1, z_pos - 1, 4)
        mc_object.setBlocks(x_pos - 4, y_pos, z_pos - 1, x_pos - 4, y_pos + 4, z_pos - 1, 85)
        # Top Left Corner
        mc_object.setBlock(x_pos + 1, y_pos - 1, z_pos + 4, 4)
        mc_object.setBlocks(x_pos + 1, y_pos, z_pos + 4, x_pos + 1, y_pos + 4, z_pos + 4, 85)
        # Top Right Corner
        mc_object.setBlock(x_pos - 4, y_pos - 1, z_pos + 4, 4)
        mc_object.setBlocks(x_pos - 4, y_pos, z_pos + 4, x_pos - 4, y_pos + 4, z_pos + 4, 85)
        # Roof
        mc_object.setBlocks(x_pos + 1, y_pos + 5, z_pos - 1, x_pos - 4, y_pos + 5, z_pos + 4, 98)

    # List of prefab objects names and their creation functions
    PREFAB_NAMES = {
        "table": _create_table,
        "vert_bookshelf": _vert_create_bookshelf,
        "hor_bookshelf": _hor_create_bookshelf,
        "stairs": _create_stairs,
        "lamp": _create_lamp,
        "plant": _create_plant,
        "central_point": _create_village_center
    }

# Hardcoded prefabs
table = Prefab([1,1], "table")
vert_bookshelf = Prefab([3,1], "vert_bookshelf")
hor_bookshelf = Prefab([1,3], "hor_bookshelf")
stairs = Prefab([4,5], "stairs")
lamp = Prefab([1,1], "lamp")
plant = Prefab([1,1], "plant")
central_point = Prefab([], "central_point")

# Prefab object list for iteration
prefab_list = [table, vert_bookshelf, hor_bookshelf, lamp, plant]

# Test case
if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    # print(table.size)
    # mc.setBlocks(-81, 69, 134, -84, 74, 137, 0)
    print(mc.getBlockWithData(-81, 69, 134))
    central_point.create(mc, 4266, 68, 5487)
