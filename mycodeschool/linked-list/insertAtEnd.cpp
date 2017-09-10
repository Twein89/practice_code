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
    temp->data = data;
    temp->next = NULL;
    if (head == NULL) {
        return temp;
    }
    Node *iter = head;
    while(iter->next != NULL) {
        iter = iter->next;
    }
    iter->next = temp; 
    return head;
    //Node *org_head = head;
    //Node *new_tail = (Node*) malloc(sizeof(Node));
    //new_tail -> data = data;
    //new_tail -> next = NULL;
    //if(head == NULL) {
    //    return new_tail;
    //}
    //while(head -> next != NULL) {
    //    head = head -> next;
    //}
    //head -> next = new_tail;
    //return org_head;
}

int main() {
    Node* A;
    A = NULL;
    //Node* temp = new Node();
    //temp->data = 2;
    //temp->next = NULL;
    //A = temp;
    A = Insert(A, 3);
    A = Insert(A, 99);
    Print(A);
    Node* B = new Node();
    B -> data = 5;
    Insert(B, 10);
    Insert(B, 20);
    Print(B);
    return 0;
}


