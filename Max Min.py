n = int(input())
k = int(input())
arr = []
item = 0
for i in range(n):
     item = int(input())
     arr.append(item)
arr = sorted(arr)
i = -1
j = k-2
m=arr[-1]
while(j < len(arr)-1):
    i=i+1
    j=j+1
    max_arr=arr[j]
    min_arr=arr[i]
    m=min(m,max_arr - min_arr)
print(m)
