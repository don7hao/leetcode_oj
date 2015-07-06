#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPowerOfTwo(int n) {
    if (n < 0x01){
        return false;
    }

    if (0x01 == n)
        return true;

    while(0x00 == n%2){
        if (0x01 == (n = n/2)){
            return true;
        }
    };

    return false;
}
