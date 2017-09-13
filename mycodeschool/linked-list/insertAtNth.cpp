#include<iostream>

using namespace std;

struct Node
{
    int data;
    Node* next;
};

void Print(Node *head) {
    Node *iter = head;
    while (iter != NULL) {
        cout << iter->data <<endl;
        iter = iter->next;
    }
}

Node* Insert(Node *head, int data) {
    Node* new_head = new Node();
    new_head -> data = data;
    new_head -> next = head;
    return new_head;
}

Node* InsertNth(Node *head, int data, int n) {
    if (n == 1) {

    }
}

int main() {
    Node* B = new Node();
    B -> data = 5;
    B = Insert(B, 3);
    Print(B);
    return 0;
}



