/*
    gen_array.c
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    /* seed random from the epoch time extracted from PCAP */
    srand(1585599106);

    /*
        An unsigned character array, the same length as the
        number of bytes in the encrypted file.

        $ du -b flag-gif.EnCiPhErEd
        374109	flag-gif.EnCiPhErEd
    */
    unsigned char *stream = malloc(374109);

    for (int i = 0; i < 374109; i++) {
        /* create a random character */
        stream[i] = rand();
        printf("%d ", stream[i]);
    }

    return 0;
}
