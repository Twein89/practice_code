#include<iostream>

using namespace std;

struct Node {
    int data;
    Node *next;
    Node *prev;
};


Node* Reverse(Node* head) {
    Node *current = head;
    while(current != NULL) {
        swap(current->next, current->prev);
        head = current;
        current = current->prev;
    }
    //while(current->next != NULL) {
    //    current = current->next;
    //}
    //Node *temp = current->next;
    //head = current->next;
    return head;
}
