#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int moveMap[4][2] = { 
	{-1, 0}, 
	{0, 1}, 
	{1, 0}, 
	{0, -1} 
};

string directions[4] = { "N", "E", "S", "W" };

int main() {
	int cases;

	for (cin >> cases; cases; cases--) {
		int n, m;
		int x, y;
		int newX, newY;
		int dir = 0;
		char command;
		string maze[60];
		
		cin >> n >> m;
		getline(cin, maze[0]);
		
		for (int i = 0; i < n; i++)
			getline(cin, maze[i]);

		cin >> x >> y;
		x--; y--;

		scanf("%c", &command);
		while (command != 'Q') {
			if (command == 'R') {
				dir = (dir + 1) % 4;
			} else if (command == 'L') {
				dir = (dir + 3) % 4;
			} else if (command == 'F') {
				newX = x + moveMap[dir][0];
				newY = y + moveMap[dir][1];

				if (newX > 0 && newX < n && newY > 0 && newY < m && maze[newX][newY] != '*') {
					x = newX;
					y = newY;
				}
			}
			scanf("%c", &command);
		}

		cout << x + 1 << " " << y + 1 << " " << directions[dir] << endl;
		
		if (cases > 1)
			cout << endl;
	}
	
	return 0;
}