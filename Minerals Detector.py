from mcpi.minecraft import Minecraft
from typing import NamedTuple 

mc = Minecraft.create()

class Coordinates(NamedTuple):
    x: int
    y: int
    z: int

Commands = ['almaz', 'железо', 'золото', 'уголь', 'exit']

def _searcher(type: int) -> Coordinates:
    pos = mc.player.getPos()

    for x in range(-5, 6, 1):
        for y in range(-5, 6, 1):
            for z in range(-5, 6, 1):
                block = mc.getBlock(pos.x+x, pos.y+y, pos.z+z)
                if block == type:
                    return Coordinates(x = x, y = y, z = z)

    return Coordinates(x = 0, y = 0, z = 0)
                


def MineralsDetector() -> None:
    message = input("Какую руду будем искать?")

    while message.lower() != 'exit':
        if message.lower() in Commands:
            if message.lower() == 'almaz':
                mc.postToChat('Searching for almaz')
                coor = _searcher(type = 56)
                if coor.x != 0 and coor.y != 0 and coor.z != 0:
                    mc.postToChat('Almaz is located:')
                    mc.postToChat(f'x: {coor.x}')
                    mc.postToChat(f'y: {coor.y}')
                    mc.postToChat(f'z: {coor.z}')
                else:
                    mc.postToChat('No almaz nearby')
            message = input()
        else:
            mc.postToChat('Нет такой команды.\nПопробуй еше раз')
    else:
        mc.postToChat('Поиск окончен')
        

MineralsDetector()
