import numpy 
import matplotlib.pyplot 
backLegSensorValues = numpy.load("datavalues.npy") 
frontLegSensorValues = numpy.load("frontLegSensorValues.npy")
matplotlib.pyplot.plot(backLegSensorValues, linewidth = 1)
matplotlib.pyplot.plot(frontLegSensorValues, linewidth = 1)
matplotlib.pyplot.legend()

matplotlib.pyplot.show()