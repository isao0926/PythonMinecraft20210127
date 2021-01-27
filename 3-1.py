from mcpi.minecraft import Minecraft
ll=Minecraft.create()

while True:
    h=ll.events.pollBlockHits()
    if len(h)>0:
        a=h[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        b=ll.getBlock(x,y,z)
        ll.postToChat("你打到了"+str(b))