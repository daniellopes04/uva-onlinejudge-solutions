#include <bits/stdc++.h>

using namespace std;

typedef struct {
    int i, j, v;
} COORD;

#define LIMIT 1005

COORD D[1000000];
int R[LIMIT], P[LIMIT];

int cmp(const void *i, const void *j) {
    static COORD *a, *b;
    a = (COORD*)i;
    b = (COORD*)j;
    
    return a->v - b->v;
}

void init(int n) {
    int i;
    for(i = 0; i < n; i++)
        R[i] = 1, P[i] = i;
}

int findp(int x) {
    if (P[x] == x) {
        return x;
    } else {
        return P[x] = findp(P[x]);
    }
}

int joint(int x, int y) {
    x = findp(x);
    y = findp(y);
    
    if(x != y) {
        if(R[x] > R[y]) {
            R[x] += R[y], P[y] = x;
        } else {
            R[y] += R[x], P[x] = y;
        }

        return 1;
    }

    return 0;
}

int main() {
    int t, n, m, r, i, j, cases = 0;
    int x[LIMIT], y[LIMIT];

    cin >> t;

    while(t--) {
        cin >> n >> r;

        for(i = 0; i < n; i++) {
            cin >> x[i] >> y[i];
        }

        init(n);
        m = 0;
        
        for(i = 0; i < n; i++) {
            for(j = i + 1; j < n; j++) {
                D[m].i = i;
                D[m].j = j;
                D[m].v = (x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]);
                m++;
            }
        }

        qsort(D, m, sizeof(COORD), cmp);
        
        int ac = 0;
        int state = 1;
        double road = 0;
        double rail = 0;
        
        r = r*r;
        
        for(i = 0; i < m; i++) {
            if(joint(D[i].i, D[i].j)) {
                if(D[i].v > r) {
                    rail += sqrt(D[i].v), state ++;
                } else {
                    road += sqrt(D[i].v);
                }
                
                ac++;

                if(ac == n-1){
                    break;
                }
            }
        }

        cout << "Case #" << ++cases << ": " << state << " " << round(road) << " " << round(rail) << endl;
    }
    return 0;
}