original_num=int(input())
num = original_num
reverse_num = 0
while num>0:
    remainder = num%10
    reverse_num = (reverse_num*10)+remainder
    num = num//10
if(reverse_num==original_num):
    print("true")
else:
    print("false")        
