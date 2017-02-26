import time

def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 : 
    # zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]


with open('../Data/mat100.dat') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            polyShape.append(line)
    del polyShape[0]
start = time.time()
matmult(polyShape,polyShape)
end = time.time()
print("Time100x100 = "+str(end - start))

with open('../Data/mat1000.dat') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            polyShape.append(line)
    del polyShape[0]
start = time.time()
matmult(polyShape,polyShape)
end = time.time()
print("Time1000x1000 = "+str(end - start))

with open('../Data/mat10000.dat') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            polyShape.append(line)
    del polyShape[0]
start = time.time()
matmult(polyShape,polyShape)
end = time.time()
print("Time10000x10000 = "+str(end - start))