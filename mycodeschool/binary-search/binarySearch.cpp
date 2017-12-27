#include<stdio.h>
#include<iostream>

using namespace std;

int BinarySearch(int A[],int n,int x) {
    int low = 0, high = n -1;
    int mid = (low + high) / 2;
    while(low <= high) {
        if(x == A[mid]) return mid;
        else if(x <= A[mid]) high = mid - 1;
        else low = mid + 1;
    }
    return -1;
}

int main() {
    int A[] = {2, 4, 5, 7, 13, 14, 15, 23};
    printf("Enter a number: ");
    int x; scanf("%d", &x);
    int index = BinarySearch(A, 8, x);
    cout<<index<<endl;
}
