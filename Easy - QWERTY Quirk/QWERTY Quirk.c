#include <stdio.h>
#include <string.h>

#define QWERTY "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
#define SIZE strlen(QWERTY)

char decode(char letter) {
    if (letter == '\n')
        return '\n';
    for (int i = 0; i < SIZE; i++)
        if (letter == QWERTY[i])
            return QWERTY[i - 1];
    return ' ';
}

int main() {
    FILE *file = fopen("inputs.txt", "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    int T;
    fscanf(file, "%d\n", &T);

    char input[256];
    char output[256];
    int ascii_sum = 0;

    for (int t = 0; t < T; t++) {
        if (fgets(input, sizeof(input), file)) {
            int i = 0;
            for (; input[i] != '\0'; i++) {
                output[i] = decode(input[i]);
                if (output[i] != '\n') {
                    ascii_sum += (int)output[i];
                }
            }
            output[i] = '\0';

            printf("%s", output);
        } else {
            printf("Error: Insufficient input lines for test cases\n");
            break;
        }
    }

    fclose(file);

    printf("\nFlag{%d}\n", ascii_sum);

    return 0;
}
