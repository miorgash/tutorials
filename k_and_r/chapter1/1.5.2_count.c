#include <stdio.h>
/* 入力される文字列をカウント；第 1 版 */
int main()
{
    long nc;

    nc = 0;
    while (getchar() != EOF)
        ++nc;
    printf("%ld\n", nc);
}
