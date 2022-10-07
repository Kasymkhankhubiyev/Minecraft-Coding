from mcpi.minecraft import Minecraft
from simple_castle import buildCastle
from EntrenceTwoStoneTowers import buildTwoTowers

import stonecastlewall as scwall


mc = Minecraft.create()

towersdist = 12
tower_length = 5
tower_height = 7
tower_width = 5
north_wall_length = 50
west_wall_length = 70
east_wall_length = 70
south_wall_length = 50





pos = mc.player.getTilePos()

buildTwoTowers(pos.x, pos.y, pos.z, towersdist, tower_length, tower_height, tower_width)
scwall.EastPropWall(pos.x-1, pos.y, pos.z+1, east_wall_length, tower_height - 2, tower_width - 2)
scwall.WestPropWall(pos.x+2*tower_length+towersdist, pos.y, pos.z+1, west_wall_length, tower_height - 2, tower_width - 2)


#Ставим башню в ближний левый угол
x = pos.x+2*tower_length+towersdist + west_wall_length
buildCastle(x, pos.y, pos.z-1, tower_height+2, tower_width+2, tower_length+2, 0)

scwall.NorthPropWall(x+2, pos.y, pos.z+6, north_wall_length, tower_height-2, tower_width-2)


#Ставим башню в ближний правый угол
x = pos.x - east_wall_length-7
buildCastle(x, pos.y, pos.z-1, tower_height+2, tower_width+2, tower_length+2, 0)

scwall.NorthPropWall(x+2, pos.y, pos.z+6, north_wall_length, tower_height-2, tower_width-2)

#Ставим башню в дальний левый угол
x = pos.x+2*tower_length+towersdist + west_wall_length
buildCastle(x, pos.y, pos.z+6+north_wall_length, tower_height+2, tower_width+2, tower_length+2, 1)


#Ставим башню в дальний правый угол
x = pos.x - east_wall_length-7
buildCastle(x, pos.y, pos.z+6+north_wall_length, tower_height+2, tower_width+2, tower_length+2, 1)

#backwall
length = west_wall_length+east_wall_length+towersdist+ 2* tower_length
scwall.WestPropWall(x+7, pos.y, pos.z+(tower_length + 2)+north_wall_length+1, length , tower_height - 2, tower_width - 2)

#расставляем башни по периметру
step = 20
for i in range(step, east_wall_length, step): #вправо -x
    if (east_wall_length - (i + 5*(i/step))) >= step:
        buildCastle(pos.x-i-5*(i/step), pos.y, pos.z-1, tower_height, tower_width, tower_length, 0)

for i in range(step, west_wall_length, step): #влево +x
    if (east_wall_length - (i + 5*(i/step))) >= step:
        buildCastle(pos.x+2*tower_length+towersdist+i, pos.y, pos.z-1, tower_height, tower_width, tower_length, 0)





