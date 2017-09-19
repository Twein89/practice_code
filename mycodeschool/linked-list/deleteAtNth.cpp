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
    Node* temp = new Node();
    temp -> data = data;
    temp -> next = head;
    return temp;
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

Node* Delete(Node *head, int n) {
    Node* temp = head;
    if (n==1) {
        head = temp -> next;
        free(temp);
        return head;
    }
    Node* iter = head;
    for(int i=0; i<n-2; i++) {
        iter = iter -> next;
    }
    temp = iter -> next;
    iter -> next = temp -> next;
    free(temp);
    return head;
}

Node* DeleteNth(Node *head, int n) {
    Node *current_node = head;
    Node *previous_node = NULL;
    for(int i=0; i<n; i++) {
        previous_node = current_node;
        current_node = current_node -> next;
    }
    if(n != 0) {
        previous_node -> next = current_node -> next;
    }
    else {
        head = head -> next;
    }
    free(current_node);
    return head;
}

int main() {
    Node* B = new Node();
    B -> data = 5;
    B = InsertNth(B, 3, 1);
    B = InsertNth(B, 88, 2);
    B = InsertNth(B, 23, 3);
    B = InsertNth(B, 110, 5);
    Print(B);
    Node* C = B;
    B = Delete(B, 2);
    //B = DeleteNth(B, 2);
    cout << "======" << endl;
    Print(B);
    cout << "------" << endl;
    Print(C);
    return 0;
}




