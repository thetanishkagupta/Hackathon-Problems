def candies(n, arr):
    res = [1]*len(arr) # giving one candy to everyone
    #FORWARD
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]: # check curr_rating > prev_rating
            res[i] = res[i-1] + 1  # if so then curr_candy = prev_candy + 1 
    
    #BACKWARD
    for i in range(len(arr)-1,0,-1):
        if (arr[i-1] > arr[i]) and (res[i-1] <= res[i]): # 'and' condition is applied so that candies value does not change on doing backward movement
            res[i-1] = res[i] + 1  
            
    return sum(res)     # sum of total candies
