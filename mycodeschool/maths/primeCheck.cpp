#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

bool prime_check(int n) {
    if(n < 2) {
        return false;
    }
    for(int div = 2; div <= sqrt(n); div++) {
        if(n % div == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int num;
    cin >> num;
    if(prime_check(num) == true) {
        cout << "PRIME" << endl;
    } else {
        cout << "NOT PRIME" << endl;
    }
    return 0;
}
