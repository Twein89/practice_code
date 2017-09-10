#include<iostream>
using namespace std;

int* arr(int* numbers, int numbersLength) {
    //int arr[2];
    int *arr = new int[2];
    arr[0] = numbers[0];
    arr[1] = numbers[numbersLength-1];
    return arr;
}

int main() {
    int numbers[5] = {2,5,8,10,9};
    int* b = arr(numbers, 5);
    cout<<*b<<endl;
    return 0;
}
