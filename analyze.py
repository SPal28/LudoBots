import numpy 
import matplotlib.pyplot 
numpy.load("data/backLegSensorValues.npy", mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')
print (backLegSensorValues)
matplotlib.pyplot.show()