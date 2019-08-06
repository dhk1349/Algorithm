#include<iostream>
#include <ctime>
#include <string>
#include<fstream>
using namespace std;

int main() {
	srand((unsigned int)time(0));
	ofstream writefile;
	ifstream readfile;

	writefile.open("test_array.csv");
	for (int i = 0;i<15000;i++) {
		writefile<< rand()<<"\n";
	}
	cout << "File created\n";
	writefile.close();
	/*
	readfile.open("test_array.csv");
	if (readfile.is_open() == true)cout << "file opend";
	string temp;
	while (getline(readfile, temp)) {
			cout << temp <<"\n";
	}
	*/
	return 1;
}