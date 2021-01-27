from mcpi.minecraft import Minecraft
ll=Minecraft.create()

x,y,z=ll.player.getTilePos()
for i in range (0,20):
    ll.setBlock(x,y-1,z+i,57)