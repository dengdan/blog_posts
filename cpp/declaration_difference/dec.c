#include <stdio.h>
extern int b;
void fn();

int main()
{
    printf("Hello World!\n");
    fn(1);
}

void fn(int a)
{
    printf("%d\n", a);
}
