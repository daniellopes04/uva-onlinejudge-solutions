#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

static const int BANDWITH_LIMIT = 1000;

int augment(vector<vector<int>> &adjacent, const vector<int> &previous, int minBandwidth, int v, int s) {
    int u = previous[v];
    minBandwidth = min(minBandwidth, adjacent[u][v]);

    if (u != s){
        minBandwidth = augment(adjacent, previous, minBandwidth, u, s);
    }

    adjacent[u][v] -= minBandwidth;
    adjacent[v][u] += minBandwidth;
    
    return minBandwidth;
}

int main() {    
    int Case = 1, n;

    while (cin >> n, n != 0) {
        vector<vector<int>> adjacent(n + 1, vector<int>(n + 1, 0));
        int s, t, c;
        int maxFlow = 0;

        cin >> s >> t >> c;

        for (int i = 1; i <= c; ++i) {
            int u, v, bandwidth;
            cin >> u >> v >> bandwidth;
            adjacent[u][v] += bandwidth;
            adjacent[v][u] += bandwidth;
        }
        
        while (maxFlow == maxFlow) {
            vector<int> previous(n + 1, -1);
            queue<int> q;
        
            previous[s] = s;
            q.push(s);

            while (!q.empty()) {
                int u = q.front();
                q.pop();
                
                for (int v = 1; v <= n; ++v)
                    if (adjacent[u][v] > 0 && previous[v] == -1) {
                        previous[v] = u;
                        q.push(v);
                    }
            }
            if (previous[t] == -1) {
                break;
            }
                
            maxFlow += augment(adjacent, previous, BANDWITH_LIMIT, t, s);
        }

        cout << "Network " << Case++ << endl;
        cout << "The bandwidth is " << maxFlow << "." << endl << endl;
    }

    return 0;
}