# Hackerearth

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
queries = int(input())
for q in range(queries):
    r1 , c1 = tuple(map(int, input().split()))
    r2 , c2 = tuple(map(int, input().split()))
    a_cell = a[r1 - 1] + b[c1 - 1]
    b_cell = a[r2 - 1] + b[c2 - 1]
    if a_cell % 2 == b_cell % 2:
        print("YES")
    else:
        print("NO")    
