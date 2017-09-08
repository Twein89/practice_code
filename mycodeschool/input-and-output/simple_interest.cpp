#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>

using namespace std;

int main() {
    float principle, rate, num_month;
    cin >> principle >> rate >> num_month;
    float result = principle * (rate / 12 * 0.01) * num_month;
    cout << fixed << setprecision(2) << result << endl;
    return 0;
}
