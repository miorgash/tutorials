#include <stdio.h>

/* 入力を出力に複写；第１版 */
int main()
{
    int c;

    while ((c = getchar()) != EOF)
        putchar(c);
}
