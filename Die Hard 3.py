import math
T = int(input())
for i in range(T):
    a,b,c = tuple(map(int, input().split()))
    greater = max(a,b)
    m = math.gcd(a,b)
    if c < greater:
        if c % m == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    
