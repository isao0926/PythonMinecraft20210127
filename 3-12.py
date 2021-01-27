from mcpi.minecraft import Minecraft
ll=Minecraft.create()
x,y,z=ll.player.getTilePos()
n=1
for i in range(8):
    for j in range(n):
        ll.spawnEntity(x,y,z,60)
    n=n*2
    ll.postToChat("這次生成了"+str(n))