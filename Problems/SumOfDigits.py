

#add all the digits of a positive integer number

def sum_of_digits(n):
    suma=0
    while n>0:
        suma=suma+n%10
        n=(n-n%10)/10
    return suma



def sum_rec(n):
    assert n>=0 and int(n)==n, "enter a positive integer only!"
    if n==0:
        return 0
    else:
        return n%10 + sum_rec(n//10)

