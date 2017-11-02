#include<iostream>

using namespace std;

int SelectionSort(int arr[], int n) {
    int min_index;
    int count = 0;
    for(int i=0; i < n; i++) {
        min_index = i;
        for(int j=i; j < n; j++) {
            if(arr[j] < arr[min_index]) {
                min_index = j;
            }
        } 
        if (arr[min_index] < arr[i]) {
            swap(arr[i], arr[min_index]);
            count++;
        }
    } 
    return count;
}

int main() {
    //int arr[] = {-1, -4, -5, -3, -11, -9, -21, -2};
    //int n = 8;
    //int num = SelectionSort(arr, n);
    //cout << num << endl;
    //for(int i=0; i < n; i++) cout<<arr[i]<<' ';
    int test_cases;
    cin>>test_cases;
    while(test_cases--) {
        int n;
        cin >> n;
        int arr[n];
        for(int i=0; i < n; i++) cin>>arr[i];
        cout << SelectionSort(arr, n) << endl;
    }
}
