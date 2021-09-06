n, k, q = map(int, input().split())
arr=list(map(int,input().split()))
k=k%n
for i in range(q):
    m=int(input())
    print(arr[m-k])

    
