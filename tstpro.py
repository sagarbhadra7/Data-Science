import numpy as np
distance = [10,15,20,25,30]
time=[0.3,0.5,0.7,0.9,0.99]
np_distance=np.array(distance)
np_time=np.array(time)
speed=np_distance/np_time
print(speed)
