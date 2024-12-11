#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>

#define MAX_ROWS 10
#define MAX_COLS 10
#define MAX_QUEUE 1000

typedef struct {
    int x, y, steps;
} Node;

typedef struct {
    Node queue[MAX_QUEUE];
    int front, rear;
} Queue;

void enqueue(Queue *q, int x, int y, int steps) {
    q->queue[q->rear++] = (Node){x, y, steps};
}

Node dequeue(Queue *q) {
    return q->queue[q->front++];
}

bool is_empty(Queue *q) {
    return q->front == q->rear;
}

int bfs(int grid[MAX_ROWS][MAX_COLS], int rows, int cols, int startX, int startY, int endX, int endY) {
    int visited[MAX_ROWS][MAX_COLS] = {0};
    int directions[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    Queue q = {.front = 0, .rear = 0};

    enqueue(&q, startX, startY, 0);
    visited[startX][startY] = 1;

    while (!is_empty(&q)) {
        Node current = dequeue(&q);

        if (current.x == endX && current.y == endY) {
            return current.steps;
        }

        for (int i = 0; i < 4; i++) {
            int nx = current.x + directions[i][0];
            int ny = current.y + directions[i][1];

            if (nx >= 0 && ny >= 0 && nx < rows && ny < cols && grid[nx][ny] == 0 && !visited[nx][ny]) {
                visited[nx][ny] = 1;
                enqueue(&q, nx, ny, current.steps + 1);
            }
        }
    }

    return -1;
}

int main() {
    FILE *file = fopen("test_cases.txt", "r");
    if (!file) {
        printf("Error: Could not open file.\n");
        return 1;
    }

    int grid[MAX_ROWS][MAX_COLS], rows, cols, startX, startY, endX, endY;
    char results[10000] = "";

    while (fscanf(file, "%d %d", &rows, &cols) != EOF) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                fscanf(file, "%d", &grid[i][j]);
            }
        }
        fscanf(file, "%d %d", &startX, &startY);
        fscanf(file, "%d %d", &endX, &endY);

        int result = bfs(grid, rows, cols, startX, startY, endX, endY);
        char buffer[10];
        sprintf(buffer, "%d", result);
        strcat(results, buffer);
    }

    fclose(file);

    printf("Flag: %s\n", results);
    return 0;
}
