#include<iostream>

using namespace std;

void PrintHelloWorld() {
    cout<<"Hello World"<<endl;
}

int *Add(int* a, int* b) {
    int* c = (int*)malloc(sizeof(int));
    *c = (*a) + (*b);
    return c;
}

int main() {
    int a = 2, b = 4;
    int* ptr = Add(&a, &b);
    cout<<*ptr<<endl;
    PrintHelloWorld();
    cout<<*ptr<<endl;
}
