n = int(input())
w = list(map(int,input().split()))[:n]
w.sort()
containers = 0
maxweight = w[0] + 4
for i in w:
    if i <= maxweight:
        continue
    containers += 1
    maxweight = i + 4

containers += 1   # Add for last container
print(containers)
