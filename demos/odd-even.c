#include <stdio.h>

int main() {

    int n = 7;
    int rem = n % 2;

    if (rem == 0) {
        printf("%d is even\n", n);
    } else {
        printf("%d is odd\n", n);
    }

    return 0;
}