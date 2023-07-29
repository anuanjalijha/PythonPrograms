def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True
    
    return False


def primeFrom2ToN(n):
    for k in range(2,n+1):
        # if k is prime and in case it is prime print k
        is_k_prime = isPrime(k)
        if(is_k_prime):
            print(k)
            
print(primeFrom2ToN(20))            
