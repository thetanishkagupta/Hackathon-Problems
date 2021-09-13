n = int(input().strip())
arr = list(map(int, input().rstrip().split()))[:n]
key = arr[-1] # last element of the array
i = n-1       # last index
while (i>0 and arr[i-1] > key):
    arr[i] = arr[i-1]
    print(*arr)
    i -= 1 
arr[i] = key    
print(*arr) 
    
