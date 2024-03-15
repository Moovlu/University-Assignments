'''
is provided coordinates from terrain smoothing.py file
use these coordinates to create plots for houses
'''

from mcpi.minecraft import Minecraft
from mcpi import block
# import random


class Smooth():

    def __init__(self, mc: Minecraft, plot_list):
        self.mc = mc
        self.plot_list = plot_list

    def smooth(self):
        mc = self.mc

        for n_plot in self.plot_list:

            c1 = n_plot[0]
            c2 = n_plot[1]

            # setting/filling in the ground
            mc.setBlocks(c1[0], c1[1], c1[2],
                         c2[0], c2[1], c2[2],
                         block.BRICK_BLOCK.id)
            # # destroying everything above(20 blocks) with air mwahahaha
            mc.setBlocks(c1[0]-1, c1[1]+1, c1[2]-1,
                         c2[0]+1, c2[1]+20, c2[2]+1,
                         block.AIR.id)
        return 'sds'
