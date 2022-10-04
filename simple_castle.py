from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()

x0 =74 # pos.x
y0 =96 # pos.y
z0 =-265 # pos.z

mc.postToChat(pos.x)
mc.postToChat(pos.y)
mc.postToChat(pos.z)

height = 10
width = 5
length = 5

mc.setBlock(x0, y0, z0, 4)

#clears area for a building

mc.setBlocks(x0, y0-1, z0, x0+length-1, y0+height-1, z0+width-1, 0)

mc.setBlocks(x0, y0-1, z0, x0+length-1, y0-1, z0+width-1, 4)

for i in range(height):
    for j in range(width):
        if (j == 0 or j==width-1):
                mc.setBlocks(x0, y0+i, z0+j, x0+length-1, y0+i, z0+j, 4)
        else:
            mc.setBlock(x0, y0+i, z0+j, 4)
            mc.setBlock(x0+length-1, y0+i, z0+j, 4)

mc.setBlocks(x0, y0+height, z0, x0+length-1, y0+height, z0+width-1, 4)

"""
Нужно добавить окна, дверь, факелы и декоративный верх
"""





