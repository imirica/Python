#calculate gcd of two numbers
#use recursion - Eucliden algorithm

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
