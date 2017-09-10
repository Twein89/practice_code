#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int addThreeNumbers(int a, int b, int c) {
    return a + b + c;
}

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int sum = addThreeNumbers(a, b, c);
    cout << sum << endl;
    return 0;
}

