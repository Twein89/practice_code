#include<iostream>

using namespace std;

struct Node
{
    int data;
    Node* link;
};


int main() {
    Node* A;
    A = NULL;
    // Node* temp = (Node*)malloc(sizeof(Node));
    Node* temp = new Node();
    // (*temp).data = 2;
    // (*temp).link = NULL;
    temp -> data = 2;
    temp -> link = NULL;
    A = temp;
    temp = new Node();
    temp -> data = 4;
    temp -> link = NULL;
    return 0;
}
