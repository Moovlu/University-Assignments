"""
Selects best possible positions for a house within the area
"""
import random
from mcpi import minecraft, block
import numpy as np
from scipy.stats import mode
import prefabs


class Terrain():
    """
    Finds plots with the given area and appends them into plot_list
    """

    def __init__(self, mc_object: minecraft):
        self.mc_object = mc_object
        self.plot_list = []
        self.town_center = []

    def plot_size(self) -> int:
        """
        Returns a random plot size from a set list
        """
        size = (15, 17, 19, 21)
        return random.choice(size)

    def clear_trees(self, x, z, SCAN_AREA):
        """
        Clears trees to fing smooth terrain
        """
        mc = self.mc_object
        CHUNK = 25

        # total_area = x-SCAN_AREA, z-SCAN_AREA, x+SCAN_AREA, z+SCAN_AREA
        for x_iter in range(x-SCAN_AREA, x+SCAN_AREA, CHUNK):
            for z_iter in range(z-SCAN_AREA, z+SCAN_AREA, CHUNK):

                x_1, y_1, z_1 = (x_iter, 62, z_iter)
                x_2, y_2, z_2 = (x_iter+CHUNK, 100, z_iter+CHUNK)

                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:acacia_log")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:birch_log")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:dark_oak_log")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:jungle_log")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:mangrove_log")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:oak_log")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:spruce_log")

                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:acacia_leaves")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:birch_leaves")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:dark_oak_leaves")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:jungle_leaves")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:mangrove_leaves")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:oak_leaves")
                mc.doCommand(
                    f"fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} air replace minecraft:spruce_leaves")

    def block_plot(self, c1, c2):
        """
        Determines whether plot placement is on valid blocks
        Prevents plots from being formed on water
        """
        mc = self.mc_object
        print("Scannning new plot for valid blocks")

        BLOCK_MATERIAL = [2, 3, 1, 12, 13, 110]
        VALID_PERCENTAGE = 0.7

        # bc_list = list(mc.getBlocks(c1[0], c1[1], c1[2], c2[0], c2[1], c2[2]))
        corner_1 = mc.getBlock(c1[0], c1[1], c1[2])
        corner_2 = mc.getBlock(c2[0], c2[1], c2[2])

        bvalid = 0
        invalid = 0

        if corner_1 in BLOCK_MATERIAL and corner_2 in BLOCK_MATERIAL:
            return [True, corner_1]
        else:
            return [False, 0]

        # for b in range(0, len(bc_list), 20):
        #     if b in BLOCK_MATERIAL:
        #         bvalid += 1
        #         block_beneath = b
        #     else:
        #         invalid += 1

        # percentage_bool = float(bvalid)/len(bc_list) >= VALID_PERCENTAGE
        # if percentage_bool:
        #     return [True, block_beneath]
        # else:
        #     return [False, 0]

    def unique_plot(self, new1, new2, mid_x, mid_z, padding):
        """
        Checks if the block position is unique
        """
        if self.plot_list:
            for val in self.plot_list:
                # Existing coordinates
                old_1 = val[0]
                old_2 = val[1]

                # Checks if new vlaues are in the range of old values, with padding applied
                if old_1[0] < old_2[0]:
                    if new1[0] in range(old_1[0] - padding, old_2[0] + padding + 1) or new2[0] in range(old_1[0] - padding, old_2[0] + padding + 1):
                        if new1[-1] in range(old_1[-1] - padding, old_2[-1] + padding + 1) or new2[-1] in range(old_1[-1] - padding, old_2[-1] + padding + 1):
                            return False

                elif old_1[0] > old_2[0]:
                    if new1[0] in range(old_2[0]-padding, old_1[0] + padding+1) or new2[0] in range(old_2[0]-padding, old_1[0]+padding+1):
                        if new1[-1] in range(old_2[-1]-padding, old_1[-1]+padding+1) or new2[-1] in range(old_2[-1]-padding, old_1[-1]+padding+1):
                            return False

                if new1[0] in range(mid_x-3-padding, mid_x+3+padding) or new2[0] in range(mid_x-3-padding, mid_x+3+padding):
                    if new1[-1] in range(mid_z-3-padding, mid_z+3+padding) or new2[-1] in range(mid_z-3-padding, mid_z+3+padding):
                        return False
        return True

    def place_plots(self):
        """
        Finds and places plots
        """
        mc_object = self.mc_object
        # Get player pos to search land around player
        x, y, z = mc_object.player.getPos()
        x = int(x)
        z = int(z)

        SCAN_AREA = 80
        mc_x = x - SCAN_AREA
        mc_z = z - SCAN_AREA
        DIFFERENT_HEIGHTS = 4
        STANDARD_DEVIATION = 1
        PADDING = 15
        MAX_PLOT_SIZE = 21
        MAX_PLOTS = 6
        PLOT_MATERIAL = block.GRASS.id

        # Clears trees surrounding the player
        self.clear_trees(x, z, SCAN_AREA)

        # Call API
        all_heights = mc_object.getHeights(
            x-SCAN_AREA, z-SCAN_AREA, x+SCAN_AREA, z+SCAN_AREA)
        # Reshape into 2D map
        height_map = np.reshape(
            all_heights, [SCAN_AREA * 2 + 1, SCAN_AREA * 2 + 1])

        x_len, z_len = height_map.shape
        block_beneath = 2

        # Scan for plot that meets requirments
        for map_x in range(x_len-MAX_PLOT_SIZE):
            for map_z in range(z_len-MAX_PLOT_SIZE):

                # NOTE: map_x is the current iteration of x, whilst mc_x is the x position in minecraft

                if len(self.plot_list) < MAX_PLOTS:

                    plot_size = self.plot_size()
                    c1 = [map_x, y, map_z]
                    c2 = [map_x+plot_size, y, map_z+plot_size]

                    plot_array = height_map[c1[0]:c2[0], c1[-1]:c2[-1]]
                    diff = plot_array.max() - plot_array.min()
                    plot_mode = mode(plot_array, axis=None)[0][0]
                    s_deviation = plot_array.std()

                    c1 = [mc_x+c1[0], plot_mode, mc_z+c1[-1]]
                    c2 = [mc_x+c2[0], plot_mode, mc_z+c2[-1]]

                    # Check if plot height difference and s_deviation meet requirments
                    if diff <= DIFFERENT_HEIGHTS and s_deviation < STANDARD_DEVIATION:
                        is_unique = False
                        block_bool = True

                        # Check if block position is unique
                        is_unique = self.unique_plot(
                            c1, c2, x+SCAN_AREA, z+SCAN_AREA, PADDING)

                        if is_unique:
                            # bool_list = self.block_plot(c1, c2)
                            # block_bool = bool_list[0]
                            # block_beneath = bool_list[1]

                            if block_bool:
                                self.smooth(c1, c2, PLOT_MATERIAL,
                                            block_beneath)
                                self.plot_list.append([c1, c2])
                                print(f'corner 1: ({c1}), corner 2: ({c2})')

        print(len(self.plot_list))
        height = mc_object.getHeight(x, z)
        self.town_center = [x-3, height, z-3]
        prefabs.central_point.create(self.mc_object, x-3, height, z-3)

        return self.plot_list

    def smooth(self, corner_1, corner_2, plot_material, material):
        """
        Smooths given terrain
        """
        mc_object = self.mc_object

        # Make the platform for the house
        mc_object.setBlocks(corner_1[0]-1, corner_1[1], corner_1[2]-1,
                            corner_2[0]+1, corner_2[1], corner_2[2]+1,
                            plot_material)
        # Destroy everything (20 blocks) above with air mwahahaha
        mc_object.setBlocks(corner_1[0]-2, corner_1[1]+1, corner_1[2]-2,
                            corner_2[0]+2, corner_2[1]+20, corner_2[2]+2,
                            block.AIR.id)

        # Create stair like indents in surroundings

        # ABOVE
        mc_object.setBlocks(corner_1[0]-3, corner_1[1] + 1, corner_1[2]-3,
                            corner_2[0]+3, corner_2[1] + 1, corner_2[2]+3,
                            block.AIR.id)

        mc_object.setBlocks(corner_1[0]-4, corner_1[1] + 2, corner_1[2]-4,
                            corner_2[0]+4, corner_2[1] + 2, corner_2[2]+4,
                            block.AIR.id)
        mc_object.setBlocks(corner_1[0]-5, corner_1[1] + 1, corner_1[2]-5,
                            corner_2[0]+5, corner_2[1] + 1, corner_2[2]+5,
                            block.AIR.id)
        # BELOW
        mc_object.setBlocks(corner_1[0]-2, corner_1[1] - 1, corner_1[2]-2,
                            corner_2[0]+2, corner_2[1] - 1, corner_2[2]+2,
                            material)
        mc_object.setBlocks(corner_1[0]-3, corner_1[1] - 2, corner_1[2]-3,
                            corner_2[0]+3, corner_2[1] - 2, corner_2[2]+3,
                            material)
        mc_object.setBlocks(corner_1[0]-4, corner_1[1] - 3, corner_1[2]-4,
                            corner_2[0]+4, corner_2[1] - 3, corner_2[2]+4,
                            material)

        # FLOWERS around house
        mc_object.setBlocks(corner_1[0]-2, corner_1[1] + 1, corner_1[2]-2,
                            corner_2[0]+2, corner_2[1] + 1, corner_2[2]+2,
                            random.randint(37, 38))


# test case
if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    obj = Terrain(mc)
    plot_list = obj.place_plots()
