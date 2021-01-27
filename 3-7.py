from mcpi.minecraft import Minecraft
ll=Minecraft.create()

x,y,z=ll.player.getTilePos()
for i in range (0,20):
    ll.setBlock(x-i,y-1,z+i,57)
    ll.setBlock(x-i-1,y-1,z+i,57)
    ll.setBlock(x-i-2,y-1,z+i,57)