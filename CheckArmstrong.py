def checkArmstrong(n):
    k = n
    length = len(str(k))
    s = 0
    while k>0:
        last_digit = k%10
        s = s+last_digit**length
        k = k//10
    if(n==s):
        print("true")
    else:
        print("false") 

n = int(input())
checkArmstrong(n)
