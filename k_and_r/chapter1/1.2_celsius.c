#include <stdio.h>

/* fahr=0.20, ..., 2300 に対して、華氏-摂氏対応表
   を印字する */
main()
{
    int fahr, celsius;
    int lower, upper, step;

    lower = 0;      /* 温度表の下限 */
    upper = 300;    /* 上限 */
    step  = 20;     /* きざみ */

    fahr = lower;
    while (fahr <= upper) {
        celsius = 5 * (fahr-32) / 9;
        printf("%3d\t%6d\n", fahr, celsius);
        fahr = fahr + step;
    }
}