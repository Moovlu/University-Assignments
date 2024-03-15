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
