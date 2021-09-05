n, k = input().split()
n = int(n)
k = int(k)
ar = list(map(int,input().strip().split()))[:n]
count=0
for i in range(n):
    for j in range(i+1, n):
        if(ar[i]+ar[j]) % k == 0:
            count += 1
print(count)          
