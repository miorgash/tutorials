#include <stdio.h>

/* celsius=0, ..., 100 に対して、摂氏-華氏対応表
   を印字する */
main()
{
    /* 1-3 & 1-4 */
    printf("celsius=0, ..., 100 に対して、摂氏-華氏対応表を印字する\n");
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;      /* 温度表の下限 */
    upper = 100;    /* 上限 */
    step  = 10;     /* きざみ */

    celsius = lower;
    while (celsius <= upper) {
        fahr = (9.0/5.0) * celsius + 32.0;
        printf("%3.0f\t%6.1f\n", celsius, fahr);
        celsius = celsius + step;
    }
}