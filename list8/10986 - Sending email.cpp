#include <bits/stdc++.h>

#define INFINITE 1000000000
#define server pair<int, int>

using namespace std;

int latency[20000];
int n, m, s, t;
vector<vector<server>> adj;

void dijkstra(int s)
{
    for(int i = 0; i<n; i++) {
        latency[i] = INFINITE;
    }

    latency[s] = 0;
    
    priority_queue<server, vector<server>, greater<server>> priority;
    priority.push(server(latency[s], s));
    
    server p;
    int t, u;

    while(!priority.empty()) {
        p = priority.top();
        priority.pop();

        t = p.first; 
        u = p.second;
        
        if(t > latency[u]) {
            continue;
        }

        for(int i = 0; i<adj[u].size(); i++) {
            if(latency[adj[u][i].first] > latency[u] + adj[u][i].second) {
                latency[adj[u][i].first] = latency[u] + adj[u][i].second;
                priority.push(server(latency[adj[u][i].first], adj[u][i].first));
            }
        }
    }
}


int main() {
    int cases, i, j;
    cin >> cases;

    for(i = 1; i <= cases; i++) {
        cin >> n >> m >> s >> t;
        adj.assign(n, vector<server>(0));
        int x, y, l;
        
        for(j = 0; j < m; j++) {
            cin >> x >> y >> l;
            adj[x].push_back(server(y, l));
            adj[y].push_back(server(x, l));
        }

        dijkstra(s);
        cout << "Case #" << i << ": ";

        if(latency[t] != INFINITE) {
            cout << latency[t] << "\n";
        } else {
            cout << "unreachable\n";
        }
    }
}