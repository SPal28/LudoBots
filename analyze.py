import numpy 
import matplotlib.pyplot 
backLegSensorValues = numpy.load("datavalues.npy") 
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()