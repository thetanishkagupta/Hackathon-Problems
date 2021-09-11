s = input()
t = input()
k = int(input().strip())
count = 0
#for loop for calculating the matching characters of both the string
for i,j in zip(s, t):  #iterate each character of s and t in i and j 
    if i == j:
        count += 1
    else:
        break
        
total_length = len(s) + len(t) #length of both the string


# CASE 1: k == total_length [yes]
# Case 2: k < total_length [No]
# Case 3: k > total_length [yes] 

if (total_length <= 2*count+k and total_length%2 == k%2 or total_length<k):
    print("Yes")
else:
    print("No")
    
