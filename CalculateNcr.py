def fact(a):
    a_fact=1 
    for i in range(1,a+1):
        a_fact = a_fact*i
    return a_fact    
    
def ncr(n,r):
    n_fact = fact(n)
    r_fact = fact(r)
    n_r_fact = fact(n-r)
    ans = n_fact//(r_fact*n_r_fact)
    return ans
print(ncr(5,2))    
