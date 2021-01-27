from mcpi.minecraft import Minecraft
ll=Minecraft.create()
x,y,z=ll.player.getTilePos()

l1=[]
l2=[]
l3=[]

for i in range(1,4):
    l1.append(1*i)
    l2.append(2*i)
    l3.append(3*i)
    
ll.setSign(x,y,z,63,0,str(l1),str(l2),str(l3))