#include <algorithm>
#include <cstdio>
 
using namespace std;
 
int queens[8];
int path[8];
 
bool isValid(int r, int c) {
    for(int j = 0; j < r; j++) {
        if(c == path[j]) {
            return false;
        }
        
        if(abs(r - j) == abs(c - path[j])) {
            return false;
        }
    }

    return true;
}
 
int search(int n) {
    int total = 100000;
    int i;

    if(n == 8) {
        return 0;
    }
 
    for(i = 0; i < 8; i++)
        if(isValid(n, i)) {
            path[n] = i;

            total = min(total, i == queens[n] ? search(n + 1) : 1 + search(n + 1));
        }
 
    return total;
}
 
int main() {
    int item, j;

    for(item = 1;; item++) {
        for(j = 0; j < 8; j++) {
            if(scanf("%d", &queens[j]) == -1) {
                return 0;
            }

            queens[j]--;
            path[j] = queens[j];
        }
 
        printf("Case %d: %d\n", item, search(0));
    }
}