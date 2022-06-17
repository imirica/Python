#positive integer
#check if it is palindrom

num=int(input("Enter a number : "))

def palindrom(num):

    original_num=num
    reversed_num=0

    while num>0:
        last_digit=num%10
        num=(num-last_digit)/10
        reversed_num=reversed_num *10+last_digit

    if original_num==reversed_num:
        return "This is a palindrom"
    else:
        return f"'{original_num}' is no palindrom"


#print(palindrom(num))

"""
num = input("Enter a number")
if num == num[::-1]:
    print("Yes its a palindrome")
else:
    print("No, its not a palindrome")
"""
