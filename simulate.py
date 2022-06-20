import pybullet_data
import time
import pybullet as p
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
for i in range (2000):
    print(i)
    time.sleep(1/1000)
    p.stepSimulation()
p.disconnect()