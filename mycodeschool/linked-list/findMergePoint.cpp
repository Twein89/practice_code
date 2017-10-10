#include<iostream>
#include<set>

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

int length(Node *head) {
    int len = 0;
    while(head != NULL) {
        len++;
        head = head->next;
    }
    return len;
}

//int FindMergePoint(Node *A, Node *B) {
//    int m = length(A);
//    int n = length(B);
//    Node *headB = B;
//    for(int i=0; i < m; i++) {
//        B = headB;
//        for(int j=0; j < n; j++) {
//            if (A == B) {
//                return A -> data;
//            }
//            B = B -> next;
//        }
//        A = A -> next;
//    }
//
//    return 0;
//}

int FindMergePoint(Node *A, Node *B) {
    set<Node *> addresses;
    int n = length(B);
    int m = length(A);

    for(int i=0; i < n; i++) {
        addresses.insert(B);
        B = B -> next;
    }

    //for(auto it = addresses.begin(); it != addresses.end(); ++it)
    //    cout << *it << endl;

    for(int i=0; i < m; i++) {
        if(addresses.find(A) != addresses.end()) {
            return A -> data;
        }
        //cout << *addresses.find(A) << "~~~~~" << *addresses.end() << endl; 
        A = A -> next;
    }
    return 0;
}

int main() {
    Node* C = new Node();
    C -> data = 7;
    C = InsertNth(C, 1, 2);
    Node* A = new Node();
    A -> data = 6;
    A -> next = C;
    A = InsertNth(A, 4, 1);
    Node* B = new Node();
    B -> data = 5;
    B -> next = C;
    B = InsertNth(B, 3, 1);
    B = InsertNth(B, 9, 1);
    //Print(A);
    //cout << "---------" << endl;
    //Print(B);
    //cout << "========" << endl;
    int r = FindMergePoint(A, B);
    cout << r << endl;
    return 0;
}
