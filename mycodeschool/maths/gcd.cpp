#include<algorithm>
#include<iostream>

using namespace std;

int euclid_gcd(int a, int b) {
    while(b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << euclid_gcd(a, b) << endl;
    return 0;
}
