import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1
x= 1.5
y= 0
z= 1.5
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute" , position = [x - 0.5, y , z - 0.5])
    pyrosim.Send_Cube(name="Backleg", pos=[x - 2 , y, z - 2] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute" , position = [x + 0.5, y , z - 0.5])
    pyrosim.Send_Cube(name="Frontleg", pos=[x - 1 , y, z - 2] , size=[length,width,height])
    pyrosim.End()
Create_Robot()