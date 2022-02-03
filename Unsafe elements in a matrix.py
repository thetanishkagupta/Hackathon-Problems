T = int(input())
for test in range(T):
    N , M = tuple(map(int, input().split()))
    matrix = []
    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    min_element , max_element = matrix[0][0] , matrix[0][0]
     
    for i in range(N):
        for j in range(M):
            if min_element > matrix[i][j]:
                min_element = matrix[i][j]
            if max_element < matrix[i][j]:
                max_element = matrix[i][j]

    rows = set()
    cols = set()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == min_element or matrix[i][j] == max_element:
                rows.add(i)
                cols.add(j)
    safe = 0
    for i in range(N):
        for j in range(M):
            if i not in rows and j not in cols:
                safe += 1
    print(safe)         
