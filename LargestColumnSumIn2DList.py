def lar_col_sum(li):
    n = len(li)
    m = len(li[0])
    max_sum=-1
    max_col_index=-1
    for j in range(m):
        sum = 0
        for i in range(n):
            sum+=li[i][j]
        if sum>max_sum:
            max_col_index = j 
            max_sum = sum
    return max_sum,max_col_index
li = [[1,2,3,4],[8,7,6,5],[9,10,11,12]]
lar_sum,lar_col_index = lar_col_sum(li)
print(lar_sum,lar_col_index)