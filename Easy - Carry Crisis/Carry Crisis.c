#include <stdio.h>

int main() {
    unsigned int input1, input2;
    int no_carry_counts = 0, carry_counts = 0;

    FILE *file = fopen("inputs.txt", "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    int T;
    fscanf(file, "%d", &T);

    for (int k = 0; k < T; k++) {

        fscanf(file, "%d %d", &input1, &input2);

        if (input1 == 0 && input2 == 0) {
            break;
        }

        int carry = 0;
        int buffer = 0;

        for (; input1 > 0 || input2 > 0; input1 /= 10, input2 /= 10) {
            if (input1 % 10 + input2 % 10 + buffer > 9) {
                carry++;
                buffer = 1;
            } else {
                buffer = 0;
            }
        }

        if (carry == 0) {
            printf("No carry operation.\n");
            no_carry_counts++;
        } else if (carry == 1) {
            printf("1 carry operation.\n");
            carry_counts++;
        } else {
            printf("%d carry operations.\n", carry);
            carry_counts++;
        }
    }

    fclose(file);

    printf("No Carry Counts = %d.\n", no_carry_counts);
    printf("Carry Counts = %d.\n", carry_counts);

    return 0;
}
