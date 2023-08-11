def wavePrint(mat, nRows, mCols):
    for j in range(mCols):
        if j%2!=0:
            for i in range(nRows-1,-1,-1):
                print(mat[i][j],end=" ")
        else:
            for i in range(nRows):
                print(mat[i][j],end=" ")        
