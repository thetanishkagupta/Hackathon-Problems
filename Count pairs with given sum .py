class Solution:
    def getPairsCount(self, arr, n, k):
        d = {}
        for i in arr:
            if (i in d):
                d[i] += 1
            else:
                d[i] = 1
        
        count = 0
        for i in arr:
            if ((k - i) in d):
                count += d[(k - i)]
            if ((k - i) == i):
                count -= 1
        return int(count/2)
