#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> juncBusyness;
typedef pair<juncBusyness, int> connection;

#define SOURCE first.first;
#define DESTINATION first.second;

int main(void) {
	int n, t = 0;

	while(cin >> n) {
		long long dist[n + 1];
		int busyness[n + 1];

		for(int i = 1; i <= n; ++i) {
			dist[i] = INT_MAX;
			cin >> busyness[i];
		}

		int junctions;
		cin >> junctions;
		vector<connection> adj(junctions);

		for(int i = 0; i < junctions; ++i) {
			int u, v;
			cin >> u >> v;
			adj[i] = connection(juncBusyness(u,v), pow(busyness[v] - busyness[u], 3));
		}

		dist[1] = 0;
		for(int i = 0; i < n - 1; ++i) {
			for(int j = 0; j < junctions; ++j) {
				int u = adj[j].SOURCE;
				int v = adj[j].DESTINATION;
				int d = adj[j].second;
				
				if(dist[u] != INT_MAX && dist[u] + d < dist[v])
					dist[v] = dist[u] + d;
			}
		}

		for(int i = 0; i < junctions; ++i) {
			int u = adj[i].SOURCE;
			int v = adj[i].DESTINATION;
			int d = adj[i].second;
			
			if(dist[u] != INT_MAX && dist[u] + d < dist[v]) {
				dist[v] = -INT_MIN;
            }
		}

		int queries;
		cin >> queries;
		cout << "Set #" << ++t << "\n"; 

		while(queries--) {
			int goal;
			cin >> goal;

			if(dist[goal] < 3 || dist[goal] == INT_MAX) {
				cout << "?\n";
            } else {
				cout << dist[goal] << "\n";
            }
		}
	}

	return 0;
}