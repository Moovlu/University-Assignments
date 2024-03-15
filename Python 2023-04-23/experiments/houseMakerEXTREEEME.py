import random
from mcpi import minecraft, block


# Setup the mcpi and find all players
mc = minecraft.Minecraft.create()
players_ids = mc.getPlayerEntityIds()
random.seed()

# Setup some basic blocks
planks = block.WOOD_PLANKS
glass = block.GLASS
air = block.AIR


class House():
    def __init__(self, corner_1:list, corner_2:list):
        self.corner_1 = corner_1
        self.corner_2 = corner_2

    def generate(self):
        # x -> [0], y -> [1], z -> [2]
        p1 = self.corner_1
        p2 = self.corner_2
        # Generate a cube
        mc.setBlocks(p1[0],p1[1],p1[2], p2[0], p2[1], p2[2], planks)
        # Hollow the cube out
        mc.setBlocks(p1[0]+1,p1[1]+1,p1[2]+1, p2[0]-1, p2[1]-1, p2[2]-1, air)
    
    def make_door(self):
        # x -> [0], y -> [1], z -> [2]
        p1 = [int(coord) for coord in self.corner_1]
        p2 = [int(coord) for coord in self.corner_2]
        side = random.randint(1,1)
        if side == 1:
            # Front (x-axis)
            door_spot = random.randint(p1[0], p2[0])
            print(p1[0], p2[0], door_spot)
            mc.setBlocks(door_spot, p1[1]+1, p1[2], door_spot, p1[1]+2, p1[2], glass)
            mc.postToChat(f"door at front:{door_spot, p1[1]+1, p1[2]}")
        elif side == 2:
            # Left (z-axis)
            door_spot = random.randint(p1[2], p2[2])
            print(p1[2], p2[2], door_spot)
            mc.setBlocks(p1[0], p1[1]+1, door_spot, p1[0], p1[1]+2, door_spot, glass)
            mc.postToChat(f"door at left:{p1[0], p1[1]+1, door_spot}")
        elif side == 3:
            # Right (z-axis)
            door_spot = random.randint(p1[2], p2[2])
            print(p1[2], p2[2], door_spot)
            mc.setBlocks(p2[0], p1[1]+1, door_spot, p2[0], p1[1]+2, door_spot, glass)
            mc.postToChat(f"door at right:{p2[0], p1[1]+1, door_spot}")
        elif side == 4:
            # Back (x-axis)
            door_spot = random.randint(p1[0], p2[0])
            print(p1[0], p2[0], door_spot)
            mc.setBlocks(door_spot, p1[1]+1, p2[2], door_spot, p1[1]+2, p2[2], glass)
            mc.postToChat(f"door at back:{door_spot, p1[1]+1, p2[2]}")


"""
######################################################
Main Code
######################################################
"""

# Check for chat commands
while True:
    # Check if player's message is a command
    for player_post in mc.entity.pollChatPosts(players_ids[0]):
        chat_msg = player_post.message
        if chat_msg.startswith("."):
            split_msg = chat_msg.split()

            # What command should be run?
            if split_msg[0].lower() == ".hi":
                mc.postToChat("HIII")

            elif split_msg[0].lower() == ".house":
                x, y, z = mc.player.getPos()
                house = House([x+2,y-1,z+2], [x+12,y+5,z+12])
                house.generate()
                house.make_door()

            else:
                mc.postToChat(f"invalid command: '{split_msg[0]}'")