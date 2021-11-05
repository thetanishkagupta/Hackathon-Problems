T=int(input())  
for i in range(T):
    x = 1
    n = int(input())  
    while True:
        s = int(bin(x)[2:].replace('1','9'))
        if s % n == 0:
            break
        x+=1
    print(s)
