#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>

using namespace std;

int main() {
    int num;
    vector<int> factors;

    cin >> num;
    for(int i = 1; i <= sqrt(num); i++) {
        if(i * i == num) {
            factors.push_back(i);
            break;
        }
        if(num % i == 0) {
            factors.push_back(i);
            factors.push_back(num/i);
        }
    }
    int sum = 0;
    for(int i = 0; i < factors.size(); i++) {
        sum += factors[i];
    }
    cout << sum << endl;
    return 0;
}
