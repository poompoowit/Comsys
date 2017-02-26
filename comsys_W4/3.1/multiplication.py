import ctypes
import time
start = time.time()
testlib = ctypes.CDLL('./multiplication.so')
testlib.myprint()
end = time.time()
print("Time = "+str(end - start))