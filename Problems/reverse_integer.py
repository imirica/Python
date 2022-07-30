#Given a signed 32-bit integer x, return x with its digits reversed. 

def reverse_integer(x):

    #create int_reversed and set it to 0
    int_reserved=0

    while x>0:

        #save the last digit of the number into a variable
        reminder=x%10

        #remove the last digit from the number
        x=x//10

        #int_reversed = int_reserved*10 + the reminder
        int_reserved=int_reserved*10 + reminder

    return int_reserved
