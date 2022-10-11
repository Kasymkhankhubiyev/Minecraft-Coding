"""
Уравнение окружности:

R^2 = x^2 + z^2

выюираем одну из осей, а вторую выставляем соответственно.

например:
1) x = x0, |X| <= R
2) z = sqrt(R^2 - x_0^2)
"""
from mcpi.minecraft import Minecraft
import math
import numpy as np
from numpy import sign

height = int
width = int
length = int
Radius = int
block_num = int

def buildCircle(x0, y0, z0, R: Radius, block: block_num) -> None:
    """
    R: Radius
    block: block type
    """

    for x in range(-1 * R, R + 1, 1):
        z = math.ceil(math.sqrt(R**2 - x**2))
        mc.postToChat(str(x)+ ': ' + str(x0 + x) + ', '
                      + str(z) + ': ' + str(z0+z))
        mc.setBlock(x0 + x, y0, z0 + z, 4)
        mc.setBlock(x0 + x, y0, z0 - z, 4)

    for z in range(-1 * R, R + 1, 1):
        x = math.ceil(math.sqrt(R**2 - z**2))

        mc.setBlock(x0 + x , y0, z0 + z, 4)
        mc.setBlock(x0 - x, y0, z0 + z, 4)
       

def buildDisk(x0, y0, z0, R: int, block: int, type=None) -> None:
    """
    R: Radius
    block: block type
    """
    for x in range(-1 * R, R + 1, 1):
        z = math.ceil(math.sqrt(R**2 - x**2))
        mc.postToChat(str(x)+ ': ' + str(x0 + x) + ', '
                      + str(z) + ': ' + str(z0+z))
        mc.setBlock(x0 + x, y0, z0 + z, 4)
        mc.setBlock(x0 + x, y0, z0 - z, 4)
        mc.setBlocks(x0 - x, y0, z0 - z, x0 + x, y0, z0 + z, 4)

    for z in range(-1 * R, R + 1, 1):
        x = math.ceil(math.sqrt(R**2 - z**2))

        mc.setBlock(x0 + x , y0, z0 + z, 4)
        mc.setBlock(x0 - x, y0, z0 + z, 4)
        

def buildCylinder(x0, y0, z0, R: Radius, H: height, block: int,
                  floor: int, ceil: int, type=None) -> None:
    """
    R: Radius
    H: Height
    block: block type
    floor - 0 - False, 1 - True
    ceil - 0 - False, 1 - True
    """
    if floor == 1:
        buildDisk(x0, y0 - 1, z0, R, block)
    for y in range(H):
        buildCircle(x0, y0 + y, z0, R, block)
    if ceil == 1:
        buildDisk(x0, y0 + H - 1, z0, R, block) 


def buildSphere(x0, y0, z0, R: Radius, block: block_num, fillin: int,
                type=None) -> None:
    """
    R: Radius
    fillin == 0 - empty sphere
    fillin == 1 - full sphere
    """
    #Нужна обработка исключений
    mc.setBlock(x0, y0, z0, block)
    if fillin == 0:
        for r in range(1, R):
            buildCircle(x0, y0+r, z0, r, block)
        for r in range(R):
            buildCircle(x0, y0+ R + r, z0, R-r, block)
    elif fillin == 1:
        for r in range(1, R):
            buildDisk(x0, y0+r, z0, r, block)
        for r in range(R):
            buildDisk(x0, y0+ R + r, z0, R-r, block)
    mc.setBlock(x0, y0+2*R, z0, block)


mc = Minecraft.create()
pos = mc.player.getTilePos()

x0, y0, z0 = pos.x, pos.y, pos.z

#buildDisk(x0, y0, z0, 10, 4)

#buildSphere(x0, y0, z0, 10, 4, 1)
#buildCylinder(x0, y0, z0, R=10, H=10, block=4, floor=1, ceil=1)
mc.setBlocks(pos.x, pos.y, pos.z, pos.x + 100, pos.y + 50, pos.z + 100, 0)
#mc.setBlocks(pos.x, pos.y-1, pos.z, pos.x +100, pos.y - 1, pos.z + 100, 2)
