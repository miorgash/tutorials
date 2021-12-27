#include <stdio.h>

/* 入力を出力に複写；第１版 */
int main()
{
    /* 1-6; 入力文字列と 1 が出力される*/
    printf("%d\n", getchar() != EOF);

    /* 1-7 EOF の値 */
    printf("%d", EOF);
}
