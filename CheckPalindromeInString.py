def palindrome(string):
    reversed_string=""
    for char in string:
        reversed_string=char+reversed_string
    if(reversed_string==string):
        print("true")
    else:
        print("false") 
        
string = str(input())        
palindrome(string)        