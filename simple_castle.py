from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def buildCastle(x0, y0, z0):
    height = 7
    width = 5
    length = 5

    mc.setBlock(x0, y0, z0, 4)

    #clears area for a building

    #mc.setBlocks(x0-7, y0, z0-7, x0+7, y0+ 17, z0+7, 0)

    mc.setBlocks(x0, y0-1, z0, x0+length-1, y0-1, z0+width-1, 4)

    for i in range(height):
        for j in range(width):
            if (j == 0 or j==width-1):
                mc.setBlocks(x0, y0+i, z0+j, x0+length-1, y0+i, z0+j, 4)
            else:
                mc.setBlock(x0, y0+i, z0+j, 4)
                mc.setBlock(x0+length-1, y0+i, z0+j, 4)

    head = 1
    state = 6

    mc.setBlocks(x0-1, y0+height, z0-1, x0+length, y0+height, z0+width, head, state)
    mc.setBlocks(x0-1, y0+height+1, z0-1, x0+length, y0+height+1, z0-1, head, state)
    mc.setBlocks(x0-1, y0+height+1, z0+width, x0+length, y0+height+1,
             z0+width, head, state)
    for i in range(width):
        mc.setBlock(x0-1, y0+height+1, z0 + i, head, state)
        mc.setBlock(x0+length, y0+height+1, z0 + i, head, state)

    #Декорируем

    mc.setBlocks(x0+length/2, y0, z0+width-1, x0+length/2, y0 + 1, z0+width-1, 0)
    mc.setBlocks(x0+length/2, y0, z0+1, x0+length/2, y0 + height, z0+1, 65, 3)
    mc.setBlock(x0-1, y0+height+2, z0-1, 50)
    mc.setBlock(x0-1, y0+height+2, z0+width, 50)
    mc.setBlock(x0+length, y0+height+2, z0-1, 50)
    mc.setBlock(x0+length, y0+height+2, z0+width, 50)
    mc.setBlock(x0-1, y0+height-1, z0, 50, 2)
    mc.setBlock(x0-1, y0+height-1, z0+width-1, 50, 2)
    mc.setBlock(x0+length, y0+height-1, z0, 50, 1)
    mc.setBlock(x0+length, y0+height-1, z0+width-1, 50, 1)

pos = mc.player.getTilePos()

x0 =74 # pos.x
y0 =96 # pos.y
z0 =-265 # pos.z

mc.postToChat(pos.x)
mc.postToChat(pos.y)
mc.postToChat(pos.z)

buildCastle(pos.x, pos.y, pos.z)
buildCastle(pos.x+13, pos.y, pos.z)
#mc.setBlocks(x0-7, y0, z0-7, x0+17, y0+ 17, z0+7, 0)


"""
Нужно добавить окна, дверь, факелы и декоративный верх
"""





