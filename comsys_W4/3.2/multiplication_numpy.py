import numpy as np
import time

with open('../Data/mat100.dat') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            polyShape.append(line)
    del polyShape[0]
start = time.time()
mx = np.matrix(polyShape)
mx = mx*mx
end = time.time()
print("Time100x100 = "+str(end - start))

start = time.time()
with open('../Data/mat1000.dat') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            polyShape.append(line)
    del polyShape[0]
start = time.time()
mx = np.matrix(polyShape)
mx = mx*mx
end = time.time()
print("Time1000x1000 = "+str(end - start))

start = time.time()
with open('../Data/mat10000.dat') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            polyShape.append(line)
    del polyShape[0]
start = time.time()
mx = np.matrix(polyShape)
mx = mx*mx
end = time.time()
print("Time10000x10000 = "+str(end - start))