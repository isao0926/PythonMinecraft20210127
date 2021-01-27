from mcpi.minecraft import Minecraft
ll=Minecraft.create()

while True:
    e=99
    h=ll.events.pollProjectileHits()
    if len(h)>0:
        a=h[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        ll.player.setTilePos(x,y,z)
        ll.spawnEntity(x,y,z,99)
        