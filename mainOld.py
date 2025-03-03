from screenToRgb import screen_to_rgb
import numpy as np

alive = True

weight0 = np.random.random((100,648000)) 
weight1 = np.random.random((100,100)) 
weight2 = np.random.random((100,100)) 
weight3 = np.random.random((11,100)) 
weights = [weight0, weight1, weight2, weight3] 

bias0 = np.random(100) #got this wrong in class originally, sorry 
bias1 = np.random(100) 
bias2 = np.random(100) 
bias3 = np.random(11) #11 controls: W, A, S, D, Mouse up, down, left, right, LShift, Lclick, Rclick 
biases = [bias0, bias1, bias2, bias3] 

controls = [pressw, pressa, …] #control functions to be coded later 

def BeauFunc(number): 
    return max(min(x+0.5,1),0) 

 

startTime = time.time() 

while alive: 
    data = np.flatten(screenToRGB()) / 256.0

    for i in range(3): 
        data = BeauFunc(weights[i]*data+biases[i]) 

    for i in data: 
        if data[i] > 0.5: 
            controls[i]() #do that thing if output is greater than 0.5 

timeToDie = time.time()-startTime
print(timeToDie)