#include <stdlib.h>
void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n)
{
    int *tab = malloc((n + m) * sizeof(int));
    int i;
    int j;
    int tabindex;

    if(tab == NULL)
        return;
    i = 0;
    j = 0;
    tabindex = 0;
    while (tabindex < n + m)
    {
        if (i >= m)
        {
            tab[tabindex] = nums2[j];
            j++;
        }
        else if (j >= n)
        {
            tab[tabindex] = nums1[i];
            i++;
        }
        else if (nums1[i] < nums2[j])
        {
            tab[tabindex] = nums1[i];
            i++;
        }
        else
        {
            tab[tabindex] = nums2[j];
            j++;
        }
        tabindex++;
    }
}