#include <stdio.h>

int sum(int a, int b)
{
    return a + b;
}



int main(void)
{
    int x;
    
    do
    {
        printf("Input a number: ");
        scanf("%d", &x);
        printf("rip you. Your value is far to high. Try a value less than 50\n\n");
    }
    while (x >= 50);

    while (x <= 100)
    {
        printf("the value as of now is: %d\n",x);
        x += 1;
    }

    printf("Here ya go: %d", x);

    return 0;
}