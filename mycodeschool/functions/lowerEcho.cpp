#include<iostream>

using namespace std;

char lowerEcho(char uppercaseLetter) {
    return tolower(uppercaseLetter);
}

int main() {
    char uppercaseLetter;
    cin>>uppercaseLetter;
    char lowercaseLetter = lowerEcho(uppercaseLetter);
    cout<<lowercaseLetter<<endl;
    return 0;
}
