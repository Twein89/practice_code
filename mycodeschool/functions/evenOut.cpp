#include<iostream>
using namespace std;

void evenOut(int* numbers, int numbersLength) {
    for (int i=0; i < numbersLength; i++) {
        if (numbers[i]%2 != 0) {
            numbers[i]--;
        }
        cout<<numbers[i]<<endl;
    }
}
int main() {
    int numbers[4] = {97,1,2,3};
    cout<<numbers<<endl;
    evenOut(numbers, 4);
}
