n = int(input())
count = 1
first_number = 1
second_number = 1
while count<n :
    next = first_number+second_number
    first_number = second_number
    second_number = next
    count = count+1
print(first_number)    
