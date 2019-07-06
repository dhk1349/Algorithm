all: examplefile

examplefile: getprint.o main.o
	g++ -o examplefile getprint.o main.o

getprint.o: getprint.h getprint.cpp
	g++ -c -o getprint.o getprint.cpp

main.o: getprint.h main.cpp
	g++ -c -o main.o main.cpp

clean:
	rm -f getprint.o main.o examplefile
