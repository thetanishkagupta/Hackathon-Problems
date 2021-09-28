#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n,temp,s=0,c=0;
    scanf("%d",&n);
    int arr[n];
    for (int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(int i = 0;i<n-1;i++)
    {
        for(int j =i+1;j<n;j++)
        {
            c = c+ 1;
            if (arr[j] <arr[i])
            { 
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
                
            }
        
        }
         s = s + 1;
    }
    for(int i =0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n%d",c);
    printf("\n%d",s);
    return 0;
}
