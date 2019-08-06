#include<iostream>
#include<fstream>
#include <string>
#include <ctime>
#include "Sorting_algorithm.h"
using namespace std;


int main() {
	int testarr[15000];
	int result=get_arr("test_array.csv",testarr,15000);


	//ERROR 
	if (result == -1) {
		cerr << "\tFailed to load array file!\n";
		return -1;
	}
	//

	
	clock_t begin = clock();

	Bubble(testarr,15000);

	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << elapsed_secs << "seconds"<<endl;




	return 1;
}
