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
frontLegSensorValues = numpy.zeros(1000)

for i in range (1000):
    print(i)
    time.sleep(1/1000)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    print(backLegSensorValues)
    print(frontLegSensorValues)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = ...,
    jointName = "...",
    controlMode = ...,
    targetPosition = ...,
    maxForce = ...)
arr = backLegSensorValues
arry = frontLegSensorValues
numpy.save("datavalues.npy", arr, allow_pickle=True, fix_imports=True)
numpy.save("frontLegSensorValues.npy", arry, allow_pickle=True, fix_imports=True)
p.disconnect()