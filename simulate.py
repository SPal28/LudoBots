import pybullet_data
import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
# def robotId():
    # open('body.urdf').readlines()
# robotId()
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
for i in range (1000):
    print(i)
    time.sleep(1/1000)
    p.stepSimulation()
backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
k = set((backLegTouch))
print(k)
p.disconnect()