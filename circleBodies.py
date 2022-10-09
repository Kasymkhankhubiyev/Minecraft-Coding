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

def buildCircle(x0, y0, z0, R, block):
    """
    R: Radius
    block: block type
    """

    for x in range(-1 * R, R + 1, 1):
        z = math.sqrt(R**2 - x**2)
        mc.postToChat(str(x)+ ': ' + str(x0 + x) + ', '
                      + str(z) + ': ' + str(z0+z))
        mc.setBlock(x0 + x, y0, z0 + z, 4)
        mc.setBlock(x0 + x, y0, z0 - z, 4)

    for z in range(-1 * R, R + 1, 1):
        x = math.sqrt(R**2 - z**2)

        mc.setBlock(x0 + x , y0, z0 + z, 4)
        mc.setBlock(x0 - x, y0, z0 + z, 4)
       

def buildDisk(x0, y0, z0, R, block):
    """
    R: Radius
    block: block type
    """
    mc.setBlock(x0, y0, z0, block)
    for r in range(R):
        buildCircle(x0, y0, z0, r, block)
        

def buildCylinder(x0, y0, z0, R, H, block):
    """
    R: Radius
    H: Height
    block: block type
    """
    for y in range(H):
        buildCircle(x0, y0 + y, z0, R, block)


def buildSphere(x0, y0, z0, R, block):
    """
    R: Radius
    """
    mc.setBlock(x0, y0, z0, block)
    for r in range(1, R):
        buildCircle(x0, y0+r, z0, r, block)
    for r in range(R):
        buildCircle(x0, y0+ R + r, z0, R-r, block)
        
        
        
    


mc = Minecraft.create()

pos = mc.player.getTilePos()

buildSphere(pos.x, pos.y, pos.z, 10, 4)
#mc.setBlocks(pos.x, pos.y, pos.z, pos.x + 100, pos.y + 50, pos.z + 100, 0)
#mc.setBlocks(pos.x, pos.y-1, pos.z, pos.x +100, pos.y - 1, pos.z + 100, 2)
