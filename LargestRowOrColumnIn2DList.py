def findLargest(arr, nRows, mCols):
    max_row_sum=-2147483648
    max_row_index=0
    max_col_sum = -2147483648
    max_col_index = 0
    for i in range(nRows):
        row_sum=0
        for j in range(mCols):
            row_sum+=arr[i][j]
        if row_sum>max_row_sum:
            max_row_sum=row_sum
            max_row_index = i 
    for j in range(mCols):
        col_sum = 0
        for i in range(nRows):
            col_sum+=arr[i][j]
        if col_sum>max_col_sum:
            max_col_sum=col_sum
            max_col_index=j 
    if max_col_sum>max_row_sum:
        print("column",max_col_index,max_col_sum)
    else:
        print("row",max_row_index,max_row_sum)    
    

