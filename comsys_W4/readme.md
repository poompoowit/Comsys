command to change C file to so file

gcc -shared -Wl,-soname,testlib -o multiplication.so -fPIC multiplication.c

command to run python multiplication.py

report:time in sec
	100	1000	10000
C	0.006	4.1	17540
numpy	0.005	3.8	84567
python	0.109	95.6	195764

run on 4770HQ @ 2.60GHz (VM 2 core with RAM:8GB SSD:50GB[swap 4GB])
