#include<iostream>

using namespace std;

const char * isLeapYear(int year) {
    if ((year%4==0 && year%100!=0) || year%400==0) {
        return "Leap year";
    }
    else {
        return "Not a leap year";
    }
}

int main() {
    cout<<isLeapYear(1900)<<endl;
    return 0;
}
