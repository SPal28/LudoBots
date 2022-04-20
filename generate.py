import time
import pybullet as p
physicsClient = p.connect(p.GUI)
for i in range (1000):
    print(i)
    time.sleep(1/60)
    p.stepSimulation()
import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
    pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
pyrosim.End()
p.disconnect()
