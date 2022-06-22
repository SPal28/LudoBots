import pybullet_data
import time
import pybullet as p
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")
def robotId():
    open('body.urdf').readlines()
robotId()
    # Joints: Step 18
    # Opened the file and read it 
    # How do I read this line into an object?
    # Should I call this function back too?
p.loadSDF("world.sdf")
for i in range (2000):
    print(i)
    time.sleep(1/1000)
    p.stepSimulation()
p.disconnect()