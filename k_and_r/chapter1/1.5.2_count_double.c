#include <stdio.h>
/* 入力される文字列をカウント；第 2 版 */
int main()
{
    double nc;

    for (nc = 0; getchar() != EOF; ++nc)
        ;
    printf("%.0f\n", nc);

}
