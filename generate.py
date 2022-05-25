import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
for x in range (0, 3):
    length = 1
    width = 1
    height = 1
    for y in range (0, 3):
        length = 1
        width = 1
        height = 1
        for z in range (0, 3):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z + 0.5] , size=[length,width,height])
            length = 0.9 * length
            width = 0.9 * width
            height = 0.9 * height
pyrosim.End()
