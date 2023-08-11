
def spiralPrint(mat, nRows, mCols):
    top,bottom,left,right=0,nRows-1,0,mCols-1
    while top<=bottom and left<=right:
        # Print the top row
        for j in range(left,right+1):
            print(mat[top][j],end=" ")
        top+=1
        # Print the right column
        for i in range(top,bottom+1):
            print(mat[i][right],end=" ")
        right-=1
        # Print the bottom row
        if top<=bottom:
            for j in range(right,left-1,-1):
                print(mat[bottom][j],end=" ")
            bottom-=1
        # Print the left column:
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(mat[i][left],end=" ")
            left+=1    
