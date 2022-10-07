from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def buildCastle(x0, y0, z0, length, height, width):
    height = height
    width = width
    length = length
    
    #mc.setBlock(x0, y0, z0, 4)

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
    mc.setBlock(x0-1, y0+height-1, z0+width-1, 50, 2) #факел
    mc.setBlock(x0+length, y0+height-1, z0, 50, 1)
    mc.setBlock(x0+length, y0+height-1, z0+width-1, 50, 1)


def buildEntrence(x0, y0, z0, length, height, width):
    mc.setBlocks(x0, y0, z0, x0+length-1, y0+height, z0+width-1, 4)
    if (length % 2) == 0:
        stpoint = length/2-2
    else:
        stpoint = length/2 - 1
    mc.setBlocks(x0+stpoint, y0, z0, x0+stpoint+3, y0+2, z0+width-1, 0)
    mc.setBlocks(x0+stpoint+1, y0+3, z0, x0+stpoint+2, y0+3, z0, 85)
    mc.setBlock(x0+stpoint+1, y0+3, z0+1, 50, 1)
    mc.setBlock(x0+stpoint+2, y0+3, z0+1, 50, 2)
    #mc.setBlocks(x0+stpoint+1, y0+3, z0+width/2, x0+stpoint+2, y0+3, z0+width/2, 50, 2)
    mc.setBlocks(x0+stpoint+1, y0+3, z0+width-1, x0+stpoint+2, y0+3, z0+width-1,85)
    mc.setBlocks(x0, y0+height, z0+width/2, x0+length, y0+height, z0+width/2, 0)

def buildTwoTowers(x0, y0, z0, towersdist, length, height, width):
    buildCastle(x0, y0, z0, length, height, width)
    buildCastle(x0+length+towersdist, y0, z0, length, height, width)
    buildEntrence(x0+5, y0, z0+1, towersdist, 5, 3)


#x0 =157 # pos.x
#y0 =94 # pos.y
#z0 =-149 # pos.z
#towersdist = 12

#pos = mc.player.getTilePos()
#mc.postToChat(str(pos.x)+', ' + str(pos.y) + ', ' + str(pos.z))

#mc.setBlocks(x0-17, y0, z0-17, x0+27, y0+ 17, z0+17, 0)
#mc.setBlocks(x0-7, y0-1, z0-7, x0+17, y0-1, z0+7, 2)
#buildTwoTowers(x0, y0, z0, towersdist)
