import pybullet_data
import time
import pybullet as p
import numpy as numpy
import pyrosim.pyrosim as pyrosim
import math
import random

math.pi
pi = math.pi
math.degrees(math.pi/2) 
90.0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

robot = robotId 

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

back_amplitude = pi/4
back_frequency = 10
back_phaseOffset = pi/4

front_amplitude = pi/4
front_frequency = 10
front_phaseOffset = 0

NUM_ITR = 1000
back_targetAngles = back_amplitude * numpy.sin(back_frequency * numpy.linspace(0, pi * 2, NUM_ITR)+ back_phaseOffset)
front_targetAngles = front_amplitude * numpy.sin(front_frequency * numpy.linspace(0, pi * 2, NUM_ITR)+ front_phaseOffset)

print(back_targetAngles)
print(front_targetAngles)
# numpy.save("targetAngleValues", targetAngles, allow_pickle=True, fix_imports=True)

# exit()

for i in range (1000):
    print(i)
    time.sleep(1/240)
    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")

    print(backLegSensorValues)
    print(frontLegSensorValues)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = b'Torso_Backleg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = back_targetAngles[i],
    maxForce = 500)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = b'Torso_Frontleg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = front_targetAngles[i],
    maxForce = 500)



# numpy.save("targetAngleValues", targetAngles, allow_pickle=True, fix_imports=True)



arr = backLegSensorValues
arry = frontLegSensorValues
numpy.save("datavalues.npy", arr, allow_pickle=True, fix_imports=True)
numpy.save("frontLegSensorValues.npy", arry, allow_pickle=True, fix_imports=True)
p.disconnect()