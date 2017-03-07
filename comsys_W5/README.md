# How to Run

cd mypapi
set the mat1000.dat path in matMult.c
correct your Makefile PAPI path
set the 7th line in Makefile to TARGETS_NTHD = matMult
make -B
./matMult
