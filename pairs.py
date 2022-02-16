def pairs(k, arr):
    dic = {}
    result = 0
    for i in arr:
        dic[i] = 1
        if i+k in dic:
            result += 1
        if i-k in dic:
            result += 1
    return result       
