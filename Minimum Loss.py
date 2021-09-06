a=int(input())
price=[int(i) for i in input().split(' ')]
SA=sorted(price)
m=999999
for i in range(len(SA)-1):
    k=SA[i+1]-SA[i]
    if k<=m and price.index(SA[i+1])<price.index(SA[i]):
        m=k    
print(m)
