import pybullet_data
import time
import pybullet as p
import numpy as numpy
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
backLegSensorValues = numpy.zeros(1000)


for i in range (1000):
    print(i)
    time.sleep(1/1000)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    print(backLegSensorValues)
arr = backLegSensorValues
numpy.save("datavalues.npy", arr, allow_pickle=True, fix_imports=True)
p.disconnect()