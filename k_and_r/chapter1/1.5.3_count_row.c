#include <stdio.h>

/* 入力の行数をカウント */
main()
{
    int c, n1;

    n1 = 0;
    while ((c = getchar()) != EOF)
        if (c == '\n')
            ++n1;
    printf("%d\n", n1);
}