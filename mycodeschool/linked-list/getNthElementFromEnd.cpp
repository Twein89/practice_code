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

int GetNthElementFromEnd(Node *head, int n) {
    int length = 0;
    Node* iter = head;
    while(iter != NULL) {
        iter = iter -> next;
        length++;
    }
    int N = length - n;
    int DistFromHead = 1;
    iter = head;
    while(iter) {
        if(N == DistFromHead) {
            return iter -> data;
        }
        iter = iter -> next;
        DistFromHead++;
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
    int N = GetNthElementFromEnd(B, 0);
    cout << N << endl;
    return 0;
}

