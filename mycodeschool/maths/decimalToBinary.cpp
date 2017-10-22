#include<iostream>
#include<algorithm>

using namespace std;

char* decimal_to_binary(int num) {
    char binary_string[101];
    int counter = 0;
    int remainder;
    if(num == 0) {
        binary_string[0] = '0';
        binary_string[1] = '\0';
        cout << binary_string << endl;
        return binary_string;
    }
    while(num != 0) {
        remainder = num % 2;
        num /= 2;
        binary_string[counter] = remainder + '0';
        counter++;
    }
    binary_string[counter] = '\0';
    reverse(binary_string, binary_string + counter);
    cout << binary_string << endl;
    return binary_string;
}

int main() {
    int number;
    cin >> number;
    decimal_to_binary(number);
    //cout << decimal_to_binary(number) << endl;
    return 0;
}
