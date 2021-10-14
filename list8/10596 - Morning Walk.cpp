
  
#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

#define LIMIT 205

int deg[LIMIT], visited[LIMIT], g[LIMIT][LIMIT];
int n, m, u, v;

void check(int x) {
	visited[x] = 1;

	for(int i = 0; i < n; i++) {
		if(g[x][i] && visited[i] == 0)
			check(i);
	}
}

int main() {
    while (cin >> n && cin >> m) {
    	memset(g, 0, sizeof(g));
        int i, j;

        for(i = 0; i < n; i++) {
            deg[i] = 0;
            visited[i] = 1;
        }

        for(i = 0; i < m; i++) {
            cin >> u;
            cin >> v;

            deg[u]++;
            deg[v]++;
            
            g[u][v] = 1;
            g[v][u] = 1;

            visited[u] = 0;
            visited[v] = 0;
        }

        int flag = 0;

        for(i = 0; i < n; i++) {
            if(deg[i] % 2 == 1) {
                flag = 1;
            }
        }

        if(flag) {
            cout << "Not Possible\n";
        } else {
        	int aux = 0;

        	for(int i = 0; i < n && aux <= 1; i++)
        		if(visited[i] == 0)
        			check(i), aux++;

        	if(aux == 1)
            	cout << "Possible\n";
            else
            	cout << "Not Possible\n";
        }
    }
    return 0;
}