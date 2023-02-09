#include "sandpiles.h"

/**
 * sandpiles_sum - computes sum of two sandpiles
 * @grid1: first sandpile
 * @grid2: second sandpile
 * Return: void
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
    int i, j;

    /* Add the values of the two grids */
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            grid1[i][j] += grid2[i][j];
        }
    }

    /* Check if the grid is unstable and perform toppling until it's stable */
    while (!is_stable(grid1))
    {
        print_grid(grid1);
        topple(grid1);
    }
}

/**
 * is_stable - validates stability of a sandpile
 * @grid: sandpile to validate
 * Return: 1 if stable, 0 on fail
 */
int is_stable(int grid[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (grid[i][j] > 3)
            {
                return 0;
            }
        }
    }
    return 1;
}

/**
 * print_grid - prints grid
 * @grid: sandpile to print
 * Return: void
 */
static void print_grid(int grid[3][3])
{
    int i, j;

    printf("=\n");
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
}

/**
 * topple - topples sandpile until it is stable
 * @grid: grid to topple and stabilize
 * Return: void
 */
void topple(int grid[3][3])
{
    int copy[3][3] = {{0}};
    int i, j;

    /**
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            copy[i][j] = 0;
        }
    } */

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (grid[i][j] > 3)
            {
                grid[i][j] = grid[i][j] - 4;
                if ((i - 1 >= 0) && (i - 1 < 3))
                {
                    copy[i - 1][j] += 1;
                }
                if ((j - 1 >= 0) && (j - 1 < 3))
                {
                    copy[i][j - 1] += 1;
                }
                if ((i + 1 >= 0) && (i + 1 < 3))
                {
                    copy[i + 1][j] += 1;
                }
                if ((j + 1 >= 0) && (j + 1 < 3))
                {
                    copy[i][j + 1] += 1;
                }
            }
        }
    }
    sandpiles_sum(grid, copy);
}
