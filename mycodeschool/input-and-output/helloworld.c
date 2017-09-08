#include<stdio.h>

int
main()
{
    char word[21];
    //gets(word);
    scanf("%200[^\n]c", word);
    printf("%s\n", word);
    return 0;
}
