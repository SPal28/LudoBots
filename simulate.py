import time
import pybullet as p
physicsClient = p.connect(p.GUI)
for i in range (1000):
    print(i)
    time.sleep(1/60)
    p.stepSimulation()
p.disconnect()