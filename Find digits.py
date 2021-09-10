t = int(input())
for i in range(t):
    count=0
    x=int(input())
    p=x
    while x>0:
        r = x % 10
        if (r != 0 and p % r == 0):
            count = count+1
        x = x // 10
    print(count)    
