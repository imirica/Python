#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

def myAtoi(s):

    #create bool and integer
    sign=True
    integer=0

    for ch in s:

        #if chracter is a digit, add it to the number
        if ch in [str(x) for x in range(10)]:
            integer=integer*10+int(ch)

        #if character is '-', bool will become false
        elif ch =="-":
            sign=False 
            
        else:
            continue
    
    if sign:
        return integer
    else:
        return -1 * integer
