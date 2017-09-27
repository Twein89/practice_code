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

int CompareLists(Node *A, Node *B) {
    while (A != NULL && B != NULL) {
        if (A->data != B->data) {
            cout << B->data << endl;
            return 0;
        }
        A = A->next;
        B = B->next;
    }
    if (A == NULL && B == NULL) {
        return 1;
    }
    else {
        return 0;
    }
}

int main() {
    Node* B = new Node();
    B -> data = 5;
    B = InsertNth(B, 3, 1);
    B = InsertNth(B, 88, 2);
    B = InsertNth(B, 23, 3);
    B = InsertNth(B, 110, 5);
    Node* C = new Node();
    C -> data = 5;
    C = InsertNth(C, 3, 1);
    C = InsertNth(C, 88, 2);
    C = InsertNth(C, 23, 3);
    C = InsertNth(C, 110, 5);
    int result = CompareLists(B, C);
    cout << result << endl;
    return 0;
}

