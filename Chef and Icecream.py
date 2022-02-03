# Codechef
# https://www.codechef.com/problems/CHFICRM


def solve(coins):
    c5, c10, c15 = 0, 0, 0 
    for coin in coins:
        if coin == 5:
            c5 += 1 
        elif coin == 10:
            if c5 >= 1:
                c10 += 1 
                c5 -= 1 
            else:
                return "NO"
        else:
            if c10 >= 1:
                c15 += 1 
                c10 -= 1 
            elif c5 >= 2:
                c15 += 1 
                c5 -= 2
            else:
                return "NO"
                
    return "YES"
    
t = int(input())
for test in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    print(solve(coins))
