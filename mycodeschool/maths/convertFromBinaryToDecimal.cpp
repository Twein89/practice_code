#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int main() {
    int test_cases; cin>>test_cases;

    while(test_cases-- > 0) {
        string binary_number; cin>>binary_number;
        reverse(binary_number.begin(), binary_number.end());

        int decimal_number = 0;
        int pow2 = 1;

        for(int place = 0; place < binary_number.size(); place++) {
            char digit = binary_number[place];
            int digit_value = digit - '0';
            decimal_number += digit_value * pow2;
            pow2 *= 2;
        }
        cout<<decimal_number<<endl;
    }
    return 0;
}
