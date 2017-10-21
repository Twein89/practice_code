#include<iostream>

using namespace std;

struct Node {
    int data;
    Node *next;
    Node *prev;
};

Node* SortedInsert(Node *head, int data) {
    Node *newNode = new Node();
    newNode->data = data;
    // empty list
    if(head == NULL) {
        newNode->next = NULL;
        newNode->prev = NULL;
        return newNode;
    }
    // at the beginning of the list
    if(head->data >= data) {
        newNode->next = head;
        newNode->prev = NULL;
        head->prev = newNode;
        head = newNode;
    } else {
        Node *current = head;
        while(current->next != NULL && current->next->data < data) {
            current = current->next;
        }
        newNode->prev = current;
        newNode->next = current->next;
        if(current->next != NULL) {
            current->next->prev = newNode;
        }
        current->next = newNode;
    }
    return head;
}

int main() {
    return 0;
}
