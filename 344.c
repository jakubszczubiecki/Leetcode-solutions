void reverseString(char* s, int sSize)
{
    int i;
    char memory;

    i = 0;
    sSize--;
    while (i < sSize)
    {
        memory = s[i];
        s[i] = s[sSize];
        s[sSize] = memory;
        i++;
        sSize--;
    }
}
#include <stdio.h>
int main(void)
{
    char string[] = "hello";
    reverseString(string, 5);
    printf("%s\n", string);
    return (0);
}