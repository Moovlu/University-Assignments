'''
trying to even the terrain to place houses using the getHeights function
1
using a while loop?

use getHeights to find if there are enough blocks with same heights
within a * b area

'''


from mcpi.minecraft import Minecraft
from mcpi import block
import random
import numpy as np
from scipy.stats import mode, stats
from collections import Counter
# import prefabs


class Terrain():

    def __init__(self, minecraft: Minecraft):
        self.mcraft = minecraft
        self.plot_list = []

    def plot_size(self):
        size = (15, 17, 19, 21)
        return random.choice(size)

    def clear_trees(self, x, z, SCAN_AREA):
        mc = self.mcraft
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

    def unique_plot(self, new1, new2, mid_x, mid_z, padding):

        if self.plot_list:

            for val in self.plot_list:
                old1 = val[0]  # existing coordinates
                old2 = val[1]

                if old1[0] < old2[0]:

                    if new1[0] in range(old1[0]-padding, old2[0]+padding+1) or new2[0] in range(old1[0]-padding, old2[0]+padding+1):
                        if new1[-1] in range(old1[-1]-padding, old2[-1]+padding+1) or new2[-1] in range(old1[-1]-padding, old2[-1]+padding+1):
                            return False

                elif old1[0] > old2[0]:

                    if new1[0] in range(old2[0]-padding, old1[0] + padding+1) or new2[0] in range(old2[0]-padding, old1[0]+padding+1):
                        if new1[-1] in range(old2[-1]-padding, old1[-1]+padding+1) or new2[-1] in range(old2[-1]-padding, old1[-1]+padding+1):
                            return False

                if new1[0] in range(mid_x-3-padding, mid_x+3+padding) or new2[0] in range(mid_x-3-padding, mid_x+3+padding):
                    if new1[-1] in range(mid_z-3-padding, mid_z+3+padding) or new2[-1] in range(mid_z-3-padding, mid_z+3+padding):
                        return False

        return True

    def block_plot(self, c1, c2):
        mc = self.mcraft

        BLOCK_MATERIAL = [2, 3, 1, 12, 13, 110]
        VALID_PERCENTAGE = 0.7

        bc_list = list(mc.getBlocks(c1[0], c1[1], c1[2], c2[0], c2[1], c2[2]))

        bvalid = 0
        invalid = 0

        for b in bc_list:
            if b in BLOCK_MATERIAL:
                bvalid += 1
                block_beneath = b
            else:
                invalid += 1

        percentage_bool = float(bvalid)/len(bc_list) >= VALID_PERCENTAGE
        if percentage_bool:
            return [True, block_beneath]
        else:
            return [False, 0]

    def clear(self):
        mc = self.mcraft
        # Get player pos to search land around player
        x, y, z = mc.player.getPos()
        x = int(x)
        z = int(z)

        SCAN_AREA = 100

        mc_x = x - SCAN_AREA
        mc_z = z - SCAN_AREA
        B_MAP_HEIGHT = 200
        DIFFERENT_HEIGHTS = 4
        STANDARD_DEVIATION = 1
        PADDING = 15
        MAX_PLOT_SIZE = 21
        MAX_NUM_PLOT = 30
        PLOT_MATERIAL = block.WOOL.id

        # mc.doCommand(f'fill {x1 62 z1 x-SCAN_AREA}')
        self.clear_trees(x, z, SCAN_AREA)

        all_heights = mc.getHeights(
            x-SCAN_AREA, z-SCAN_AREA, x+SCAN_AREA, z+SCAN_AREA)

        height_map = np.reshape(
            all_heights, [SCAN_AREA * 2 + 1, SCAN_AREA * 2 + 1])

        # Make 3d array for blocks
        all_blocks = list(mc.getBlocks(
            x-SCAN_AREA, 0, z-SCAN_AREA, x+SCAN_AREA, B_MAP_HEIGHT, z+SCAN_AREA))

        block_map = np.reshape(
            all_blocks, [SCAN_AREA * 2 + 1, B_MAP_HEIGHT + 1, SCAN_AREA * 2 + 1])

        x_len, z_len = height_map.shape
        # block_beneath = 2

        for map_x in range(x_len-MAX_PLOT_SIZE):
            for map_z in range(z_len-MAX_PLOT_SIZE):
                # if len(self.plot_list) < MAX_NUM_PLOT:
                plot_size = self.plot_size()
                c1 = [map_x, y, map_z]
                c2 = [map_x+MAX_PLOT_SIZE, y, map_z+MAX_PLOT_SIZE]

                plot_array = height_map[c1[0]:c2[0], c1[-1]:c2[-1]]
                diff = plot_array.max() - plot_array.min()
                plot_mode = mode(plot_array, axis=None)[0][0]
                std = plot_array.std()

                c1 = [mc_x+c1[0], plot_mode, mc_z+c1[-1]]
                c2 = [mc_x+c2[0], plot_mode, mc_z+c2[-1]]

                # Check if plot height difference and standard deviation meet requirments
                if diff <= DIFFERENT_HEIGHTS and std < STANDARD_DEVIATION:
                    unique_bool = False
                    block_bool = True

                    unique_bool = self.unique_plot(
                        c1, c2, x+SCAN_AREA, z+SCAN_AREA, PADDING)

                    if unique_bool:
                        bool_list = self.block_plot(c1, c2)
                        block_bool = bool_list[0]
                        block_beneath = bool_list[1]

                        if len(self.plot_list) < MAX_NUM_PLOT and block_bool:
                            self.smooth(c1, c2, PLOT_MATERIAL, block_beneath)
                            self.plot_list.append([c1, c2])
                            print(f'corner 1: ({c1}), corner 2: ({c2})')

        #                     if block_bool:
        #                         # Find what block to fill in surrounding land with
        #                         # block_height = height_map[map_x, map_z]
        #                         # block_beneath = block_map[map_x, block_height, map_z]

        print(len(self.plot_list))

        # prefabs.village_centre.create(mc, x-3, y, z-3)

        return self.plot_list

    def smooth(self, c1, c2, plot_material, material):
        mc = self.mcraft

        # Set/fill in the ground
        mc.setBlocks(c1[0], c1[1] - 1, c1[2],
                     c2[0], c2[1] - 1, c2[2],
                     material)
        # Make the platform for the house
        mc.setBlocks(c1[0], c1[1], c1[2],
                     c2[0], c2[1], c2[2],
                     plot_material)
        # Destroy everything (20 blocks) above with air mwahahaha
        mc.setBlocks(c1[0]-1, c1[1]+1, c1[2]-1,
                     c2[0]+1, c2[1]+20, c2[2]+1,
                     block.AIR.id)


# Test case
if __name__ == "__main__":
    from mcpi.minecraft import Minecraft
    # from create_plot import Smooth

    from terrain_smoothing import Terrain

    mc = Minecraft.create()
    mc.doCommand("gamerule doDaylightCycle false")
    mc.doCommand("time set day")
    mc.doCommand("weather clear")

    # x, y, z = mc.player.getPos()

    tobj = Terrain(mc)
    plot_list = tobj.clear()
