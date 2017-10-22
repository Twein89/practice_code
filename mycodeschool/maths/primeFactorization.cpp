#include<iostream>
#include<cmath>

using namespace std;

int main() {
    int N;
    cin >> N;
    int count;
    for(int i = 2; i <= sqrt(N); i++) {
        count = 0;
        while(N%i == 0) {
            count++;
            N /= i;
        }

        if(count > 0) {
            cout << i << "^" <<count;
            if(N > 1) cout << "*";
        }
    }
    if(N > 1) {
        cout << N << "^1";
    }
    cout << endl;
}
