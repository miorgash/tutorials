#include <stdio.h>
#define IS_SPACE  1
#define NOT_SPACE 0

main ()
{
    int c, state;
    state = NOT_SPACE;
    while ((c = getchar()) != EOF)
    {
        /* 判定 */
        if (c == ' ')
            state = IS_SPACE;
        if (c != ' ') {
            if (state == IS_SPACE) {
                putchar(' ');
                putchar(c);
                state = NOT_SPACE;
            } else {
                putchar(c);
            }
        }
    }
}