def plantTree(x,y,z):
    ll.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    ll.setBlocks(x,y,z,x,y+4,z,17)

from mcpi.minecraft import Minecraft
ll=Minecraft.create()
x,y,z=ll.player.getTilePos()
for i in range(10):
    plantTree(x+i*5,y,z)