#include <iostream>
#include <fstream>
#include <string>
#include "Sorting_algorithm.h"
using namespace std;

int get_arr(string filename, int arr[], int size) {
	ifstream arrfile;
	string temp;
	int cnt = 0;
	//arr.open("C:\\Users\\dhk13\\Desktop\\Algorithm_assignment\\random_num_generator\\test_array.csv");
	arrfile.open(filename);
	if (arrfile.is_open() == false)return -1;

	cout << "File successfully opened\n";

	while (getline(arrfile, temp)) {
		arr[cnt] = atoi(temp.c_str());
		cnt++;
	}
	cout << cnt << " of integer array loaded\n\n";

	return 1;
}

void Bubble(int arr[], int size) {//sort in ascending order
	bool changed;
	int iterator = size - 1;
	int temp;
	do {
		changed = false;
		for (int i = 0;i<iterator;i++) {
			if (arr[i]>arr[i+1]) {//swap case
				temp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = temp;
				changed = true;
			}
		}
		iterator--;
		/*
		for (int i = 0; i < size; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << std::endl;
		*/
	} while (changed == true);
}

void My_sort(int arr[], int size) {
	
}