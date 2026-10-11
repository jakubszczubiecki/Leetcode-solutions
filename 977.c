#include <stdio.h>
#include <stdlib.h>

int *sortedSquares(int *nums, int numSize, int *returnSize)
{
    int *result;
    int i;
    int j;
    int extra_memory;

    result = malloc(numSize * sizeof(int));
    if (result == NULL)
        return (NULL);

    i = 0;
    while (i < numSize)
    {
        result[i] = nums[i] * nums[i];
        i++;
    }

    i = 0;
    while (i < numSize - 1)
    {
        j = 0;
        while (j < numSize - 1 - i)
        {
            if (result[j] > result[j + 1])
            {
                extra_memory = result[j];
                result[j] = result[j + 1];
                result[j + 1] = extra_memory;
            }
            j++;
        }
        i++;
    }

    *returnSize = numSize;
    return (result);
}

int main(void)
{
    int nums[] = {-4, -1, 0, 3, 10};
    int numSize = 5;
    int returnSize;
    int *result;
    int i;

    result = sortedSquares(nums, numSize, &returnSize);

    if (result == NULL)
        return (1);

    i = 0;
    while (i < returnSize)
    {
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    free(result);
    return (0);
}