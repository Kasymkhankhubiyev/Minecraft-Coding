from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x0 = 155.
y0 = 90.
z0 = -336.

#pos = mc.player.getTilePos()

#mc.setBlock(pos.x+3,

N = 5
distance = 3

height = 5 #y
length = 5 #x
width = 5 #z

def build_simple_house(x0, y0, z0, floor, silling, walls, floor_state):
    for i in range(width):
        for j in range(length):
            mc.setBlock(x0+j, y0, z0+i, floor, floor_state)

    for k in range(1, height-1):
        for i in range(length): #ставим стену
            if (i == 2 and k == 2):
                mc.setBlock(x0+i, y0+k, z0, 160)
            else:
                mc.setBlock(x0+i, y0+k, z0, walls)
        for j in range(1, width-1):
            mc.setBlock(x0, y0+k, z0+j, walls)
            mc.setBlock(x0+length-1, y0+k, z0+j, walls)
        for j in range(length):
            if (k == 1) and (j == 2):
                mc.setBlock(x0+j, y0+k, z0+width, 0)
            elif (k == 2) and (j == 2):
                pass
            else:
                mc.setBlock(x0+j, y0+k, z0+width-1, walls)

    for i in range(width):
        for j in range(length):
            mc.setBlock(x0+j, y0+height-1, z0+i, silling, floor_state)

for i in range(N):
    #build_simple_house(x0, y0, z0, 0, 0, 0, 0)
    build_simple_house(x0, y0, z0, 179, 179, 179, 2)
    x0 += distance + length
        
        

