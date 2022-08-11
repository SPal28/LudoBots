import numpy 
import matplotlib.pyplot as plt
import math 
math.pi
pi = math.pi
#backLegSensorValues = numpy.load("datavalues.npy") 
#frontLegSensorValues = numpy.load("frontLegSensorValues.npy")
#matplotlib.pyplot.plot(backLegSensorValues, linewidth = 1)
#matplotlib.pyplot.plot(frontLegSensorValues, linewidth = 1)
#matplotlib.pyplot.legend()

targetAngleValues = numpy.load("targetAngleValues.npy")
x = numpy.linspace(-pi/4, pi/4, 201)
plt.plot(x, numpy.sin(x))
plt.xlabel('steps')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()