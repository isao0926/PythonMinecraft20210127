from mcpi.minecraft import Minecraft
ll=Minecraft.create()
x,y,z=ll.player.getTilePos()
b=18
h=(b//2)+1
for i in range(h):
    x1=x+i
    y1=y+i
    z1=z+i
    
    x2=x+b-i
    z2=z+b-i
    ll.setBlocks(x1,y1,z1,x2,y1,z2,57)
    