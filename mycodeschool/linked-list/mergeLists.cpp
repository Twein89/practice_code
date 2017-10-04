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

Node* InsertNth(Node *head, int data, int n) {
    Node* temp = new Node();
    temp -> data = data;
    temp -> next = NULL;
    if (n == 1) {
        temp -> next = head;    
        return temp;
    }
    Node* iter = head; 
    for (int i=1; i<n-1; i++) {
        iter = iter -> next;
    }
    if(iter -> next != NULL) {
        Node* after = iter -> next;  
        iter -> next = temp;
        temp -> next = after;
    }
    else {
        iter -> next = temp;
    }
    return head;
}

Node* MergeLists(Node *A, Node *B) {
    if (A == NULL && B == NULL) {
        return NULL;
    }
    else if (A != NULL && B == NULL) {
        return A;
    }
    else if (A == NULL && B != NULL) {
        return B;
    }
    else if (A -> data <= B -> data) {
        A -> next = MergeLists(A -> next, B);
        return A;
    }
    else {
        B -> next = MergeLists(A, B -> next);
        return B;
    }
}

int main() {
    Node* B = new Node();
    B -> data = 2;
    B = InsertNth(B, 9, 2);
    B = InsertNth(B, 30, 3);
    B = InsertNth(B, 60, 4);
    B = InsertNth(B, 110, 5);
    //Print(B);
    Node* C = new Node();
    C -> data = 5;
    C = InsertNth(C, 7, 2);
    C = InsertNth(C, 25, 3);
    C = InsertNth(C, 50, 4);
    C = InsertNth(C, 70, 5);
    Node *M = MergeLists(B, C);
    Print(M);
    return 0;
}

