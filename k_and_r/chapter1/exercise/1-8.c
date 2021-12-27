#include <stdio.h>

main()
{
    int c, nl, nt, nn;
    while ((c = getchar()) != EOF)
    {
        if (c == ' ')
            ++nl;
        if (c == '\t')
            ++nt;
        if (c == '\n')
            ++nn;
    }
    printf("%d, %d, %d", nl, nt, nn);
}