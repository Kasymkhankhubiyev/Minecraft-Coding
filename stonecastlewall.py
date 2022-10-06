from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def WesrPropWall(x0, y0, z0, length, height, width):
    #в сторону роста оси Х

    mc.setBlocks(x0, y0, z0, x0+length-1, y0+height-1, z0+width-1, 98)
    mc.setBlocks(x0, y0+height-1, z0+1, x0+length-1, y0+height-1, z0+width-2, 0)

    for i in range(1, length, 2):
        mc.postToChat(x0+i)
        mc.setBlock(x0+i, y0+height-1, z0, 44)
        mc.setBlock(x0+i, y0+height-1, z0+width-1, 44)

def EastPropWall(x0, y0, z0, length, height, width):
    #в сторону убывания оси Х
    
    mc.setBlocks(x0-length+1, y0, z0, x0, y0+height-1, z0+width-1, 98)
    mc.setBlocks(x0-length+1, y0+height-1, z0+1, x0, y0+height-1, z0+width-2, 0)

    for i in range(-1*length+1, 1, 2):
        mc.postToChat(x0+i)
        mc.setBlock(x0+i, y0+height-1, z0, 44)
        mc.setBlock(x0++i, y0+height-1, z0+width-1, 44)

def NorthPropWall(x0, y0, z0, length, height, width):
    #В сторону роста оси Z
    
    mc.setBlocks(x0, y0, z0, x0+width-1, y0+height-1, z0+length-1, 98)
    mc.setBlocks(x0+1, y0+height-1, z0, x0+width-2, y0+height-1, z0+length-1, 0)

    for i in range(1, length, 2):
        mc.postToChat(z0+i)
        mc.setBlock(x0, y0+height-1, z0+i, 44)
        mc.setBlock(x0+width-1, y0+height-1, z0+i, 44)

def SouthPropWall(x0, y0, z0, length, height, width):
    #в сторону убывания оси Z
    
    mc.setBlocks(x0, y0, z0-length+1, x0+width-1, y0+height-1, z0, 98)
    mc.setBlocks(x0+1, y0+height-1, z0-length+1, x0+width-2, y0+height-1, z0, 0)

    for i in range(-1*length+1, 1, 2):
        mc.postToChat(z0+i)
        mc.setBlock(x0, y0+height-1, z0+i, 44)
        mc.setBlock(x0+width-1, y0+height-1, z0+i, 44)



x0 = 74
y0 = 96
z0 = -265
length = 10
width = 3
height= 5

mc.setBlocks(x0-17, y0, z0-17, x0+17, y0+ 17, z0+17, 0)

NorthPropWall(x0, y0, z0, length, height, width)

