#include <bits/stdc++.h>
#include <cmath>
using namespace std;

typedef long long ll;

#define endl '\n'

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t;
    while (t--) {
        ll n;
        cin >> n;
        if (n == 1) {
            cout << 0 << endl;
        } else {
            cout << (ll)ceil(sqrt(1.0L * n)) - 1 << endl;
        }
    }
}