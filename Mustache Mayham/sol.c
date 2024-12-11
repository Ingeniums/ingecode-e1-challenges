#include <stdio.h>
#include <string.h>

#define MAX_LINE 1024

int count_occurrences(const char *str, const char *seq)
{
    int count = 0;
    const char *temp = str;
    while ((temp = strstr(temp, seq)) != NULL)
    {
        count++;
        temp += strlen(seq);
    }
    return count;
}

void solve_challenge(const char *filename)
{
    FILE *file = fopen(filename, "r");
    if (!file)
    {
        printf("Error: Could not open file %s\n", filename);
        return;
    }

    char line[MAX_LINE];
    char final_binary[MAX_LINE] = "";
    char random_string[MAX_LINE];

    while (fgets(line, sizeof(line), file))
    {
        if (strncmp(line, "Random String:", 14) == 0)
        {
            sscanf(line + 14, "%[^\n]", random_string);
            int count = count_occurrences(random_string, ":-|");
            strcat(final_binary, count % 2 == 0 ? "0" : "1");
        }
    }

    fclose(file);
    printf("Final Binary Code: %s\n", final_binary);
}

int main()
{
    solve_challenge("test_cases.txt");
    return 0;
}
