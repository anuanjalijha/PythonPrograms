def rowWiseSum(mat, nRows, mCols):
    for i in range(nRows):
        row_sum = 0
        for j in range(mCols):
            row_sum+=mat[i][j]
        print(row_sum,end=" ")     
