#include<iostream>
#include <algorithm>
#define INF 999999
using namespace std;
/*
=====Minimal Coin Problem=====
Selecting minimul numbers of coin to make certain amount of coin.
Coin with greedy algorithm sometimes fails to give right answer.
However with dynamic programming, function will return correct answer efficiently.
*/
int MinimalCoin(int x) {
	int coin[3] = { 1,3,4 };
	if (x < 0) return INF;
	if (x == 0) return 0;
	int best = INF;
	for (int c : coin) {
		best = min(best, MinimalCoin(x - c) + 1);
	}
	return best;
}

int MinimalCoin2(int x, bool ready[], int value[]) {
	int coin[3] = { 1,3,4 };
	if (x < 0) return INF;
	if (x == 0) return 0;
	if (ready[x]) return value[x];
	int best = INF;
	for (int c : coin) {
		best = min(best, MinimalCoin(x - c) + 1);
	}
	return best;
}

/*
=====Longest Increasing Subsequence=====
Getting solution by using dynamic programming
*/

int LIS_recursive(int x, int sec[]) {
	int length = 1;
	for (int i = 0; i < x; i++) {
		if (sec[i] < sec[x]) {
			length = max(length, LIS_recursive(i, sec) + 1);
		}
	}
	return length;
}

int LIS() {
	int sequence[8] = {6,2,5,1,7,4,8,3};
	cout << "Finding Longest increasing sequence with sequence\n";
	for (int i = 0;i<8;i++) {
		cout <<"\t" << sequence[i];
	}
	cout << endl<<"Location: ";
	int x;
	cin >> x;
	cout<<"result: "<<LIS_recursive(x, sequence)<<endl;
	return 1;
}

int main() {
	/*
	cout << "\tOptimal process for coin problem (coins worth 1,3,4)\n";
	bool ready[10] = { false };
	int value[10] = { INF };
	int result;
	int x;
	do {
		cout << "1. How much coin will you get?\n";
		cin >> x;
		result = MinimalCoin2(x, ready, value);
		cout << "You need lead " << result << " coins" << endl;
	} while (result != INF);
	*/

	do {
		LIS();

	} while (true);
	return 1;
}