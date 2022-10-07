"""
высота постройки 13 блоков
ширина (по z) 9 блоков
длина 15 блоков
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def build(x0, y0, z0):

    file = open('CakeShopTent.txt', 'r')

    datas = []
    for line in file:
        data = line.split(',')
        indexes = [int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4])]
        datas.append(indexes)

    file.close()
    
    for i in range(len(datas)):
        mc.setBlock(x0 + datas[i][0], y0 + datas[i][1],
                    z0 + datas[i][2], datas[i][3], datas[i][4])
                
