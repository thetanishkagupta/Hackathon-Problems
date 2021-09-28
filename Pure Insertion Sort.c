#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n,current,j,c,s=0;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(int i=1;i<n;i++)
    {
        current = arr[i];
        j = i - 1;
        while(arr[j] > current && j>=0)
        {   
            arr[j+1] = arr[j];
            j = j - 1;
            s = s + 1;
            
        }
        arr[j+1] = current;
    }
    for(int i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    c = 0.5*(n*n - n);
    printf("\n%d %d",c,s);
    return 0;
}
