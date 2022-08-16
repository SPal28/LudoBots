import numpy 
import matplotlib.pyplot as plt
import math 
math.pi
pi = math.pi
NUM_ITR = 1000

#backLegSensorValues = numpy.load("datavalues.npy") 
#frontLegSensorValues = numpy.load("frontLegSensorValues.npy")
#matplotlib.pyplot.plot(backLegSensorValues, linewidth = 1)
#matplotlib.pyplot.plot(frontLegSensorValues, linewidth = 1)
#matplotlib.pyplot.legend()

targetAngleValues = numpy.load("targetAngleValues.npy")
x = numpy.linspace(0, 1000, NUM_ITR)
plt.plot(x, targetAngleValues)
plt.xlabel('steps')
plt.ylabel('sin(x)')
plt.axis('tight')

plt.show()