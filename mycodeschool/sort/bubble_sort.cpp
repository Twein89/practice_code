#include<iostream>

using namespace std;

int BubbleSort(int arr[], int n) {
    int flag;
    int count = 0;
    for(int i=0; i < n; i++) {
        flag = 0;
        for(int j=0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
                flag = 1;
                count++;
            }
        }
        if(flag == 0)break;
    }
    return count;
}

int main() {
    //int arr[] = {-1, -4, -5, -3, -11, -9, -21, -2};
    //int n = 8;
    //int num = BubbleSort(arr, n);
    //cout << num << endl;
    //for(int i=0; i < n; i++) cout<<arr[i]<<' ';
    int test_cases;
    cin>>test_cases;
    while(test_cases--) {
        int n;
        cin >> n;
        int arr[n];
        for(int i=0; i < n; i++) cin>>arr[i];
        cout << BubbleSort(arr, n) << endl;
    }
    return 0;
}
