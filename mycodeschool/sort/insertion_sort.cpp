#include<iostream>

using namespace std;

int InsertionSort(int arr[], int n) {
    int value;
    int hole;
    int count = 0;
    for(int i=1; i < n; i++) {
        value = arr[i];
        hole = i;
        while(hole > 0 && (arr[hole - 1] > value)) {
            arr[hole] = arr[hole - 1];
            hole = hole - 1;
            count++;
        }
        if (arr[hole] != value) {
            arr[hole] = value;
            count++;
        }
    }
    return count;
}

int main() {
    //int arr[] = {2, 4, 1, 3, 5};
    //int n = 5;
    //int num = InsertionSort(arr, n);
    //cout << num << endl;
    //for(int i=0; i < n; i++) cout<<arr[i]<<' ';
    
    int test_cases;
    cin>>test_cases;
    while(test_cases--) {
        int n;
        cin >> n;
        int arr[n];
        for(int i=0; i < n; i++) cin>>arr[i];
        cout << InsertionSort(arr, n) << endl;
    }
}

