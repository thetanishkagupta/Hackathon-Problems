n = int(input())
arr = list(map(int,input().split()))[:n]
arr.sort()
ans = 1
prev = arr[0]
for i in range(1,n):
    if(arr[i] - prev) > 4:
        prev = arr[i]
        ans = ans + 1
        
print(ans)        
