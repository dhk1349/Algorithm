#include<iostream>
#include <algorithm>
#define INF 999999
using namespace std;
/*
Selecting minimul numbers of coin to make certain amount of coin.
Coin with greedy algorithm sometimes fails to give right answer.
However with dynamic programming, function will return correct answer efficiently.
*/



int solve(int x) {
	int coin[3] = { 1,3,4 };
	if (x < 0) return INF;
	if (x == 0) return 0;
	int best = INF;
	for (int c : coin) {
		best = min(best, solve(x - c) + 1);
	}
	return best;
}


int solve2(int x, bool ready[], int value[]) {
	int coin[3] = { 1,3,4 };
	if (x < 0) return INF;
	if (x == 0) return 0;
	if (ready[x]) return value[x];
	int best = INF;
	for (int c : coin) {
		best = min(best, solve(x - c) + 1);
	}
	return best;
}
void main() {
	cout << "\tOptimal process for coin problem (coins worth 1,3,4)\n";
	bool ready[10] = { false };
	int value[10] = { INF };
	int result;
	int x;
	do {
		cout << "1. How much coin will you get?\n";
		cin >> x;
		result = solve2(x, ready, value);
		cout << "You need lead " << result << " coins" << endl;
	} while (result != INF);
}