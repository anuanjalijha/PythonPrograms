def findGcd(x, y):
    gcd = 1 
    if x>y:
        max = x
    else:
        max = y
        
    for i in range(2,max+1):
        if(x%i==0 and y%i==0):
            gcd = i
    return gcd
