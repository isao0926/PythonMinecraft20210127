from mcpi.minecraft import Minecraft
ll=Minecraft.create()

while True:
    h=ll.events.pollProjectileHits()
    if len(h)>0:
        a=h[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        ll.createExplosion(x,y,z,power=100)