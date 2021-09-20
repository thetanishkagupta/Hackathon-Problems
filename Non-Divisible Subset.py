n, k = map(int,raw_input().strip().split(" "))
s = map(int,raw_input().strip().split(" "))

#count is a variable and counts is a list

counts = [0] * k  #size of list is k
for num in s:
    counts[num % k] += 1  #finding the remainder 

count = min(counts[0], 1)
for i in range(1, k//2+1):  #finding pair whose sum is not perfectly divisible by k
    if i != k - i:
        count += max(counts[i], counts[k-i])
if k % 2 == 0: 
    count += 1

print count
