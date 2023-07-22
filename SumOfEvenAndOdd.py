n = int(input())
sum_of_even_digits=0
sum_of_odd_digits=0
while n>0:
    digits = n%10
    n = n//10
    if(digits%2==0):
        sum_of_even_digits = sum_of_even_digits+digits
    else:
        sum_of_odd_digits = sum_of_odd_digits+digits    
print(sum_of_even_digits," ",sum_of_odd_digits)