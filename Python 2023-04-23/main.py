"""
The main file of this project. Connects all other modules.
"""
from mcpi import minecraft
# import terrain_selection as sel
# import terrain_smoothing as smooth
# import house
import path_finding as path
# import prefabs
from terrain_selection import Terrain
from house import House
import house_population as pop

# Create minecraft object
mc = minecraft.Minecraft.create()

mc.doCommand("gamerule doDaylightCycle false")
mc.doCommand("time set noon")

# Cool main code goes here
plot_obj = Terrain(mc)
plot_list = plot_obj.place_plots()

door_path_pos = []
house_locations = []


for plot in plot_list:
    mc_house = House()
    plot = [[plot[0][0], plot[0][2], plot[0][1] + 1],[plot[1][0], plot[1][2], plot[1][1] + 1]]
    print(f"currently doing {plot}")
    mc_house.house(plot[0], plot[1])

    door_path_pos.append(mc_house.frontdoor_pos)
    house_locations.append(mc_house.house_size)

    staircase = [[0, 0], [0, 0]]

    if mc_house.house_stories == 2:
        staircase = pop.place_staircase(mc, mc_house.room_coords)
    pop.populate_rooms(mc, mc_house.room_coords, staircase)


# Create new paths
print(f"HOUSE LOCATIONS {house_locations}")
print(f"TOWN CENTER {plot_obj.town_center}")
for door in door_path_pos:
    path_obj = path.Path(mc, door, plot_obj.town_center, house_locations)

mc.doCommand("kill @e[type=minecraft:item]")