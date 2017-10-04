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

int HasLoop(Node* head) {
    Node* fast_ptr = head;
    Node* slow_ptr = head;
    while(fast_ptr->next != NULL && fast_ptr->next->next != NULL) {
        fast_ptr = fast_ptr->next->next;
        slow_ptr = slow_ptr->next;
        if(fast_ptr == slow_ptr) {
            return 1;
        }
    }
    return 0;
}

int main() {
    Node* B = new Node();
    B -> data = 2;
    B = InsertNth(B, 9, 2);
    B = InsertNth(B, 30, 3);
    B = InsertNth(B, 30, 4);
    B = InsertNth(B, 110, 5);
    Node* k = new Node();
    k -> data = 666;
    cout << B->next->next->data << endl;
    B->next->next->next = k;
    k->next = B->next;
    //Print(B);
    int r = HasLoop(B);
    cout << r << endl;
    return 0;
}


