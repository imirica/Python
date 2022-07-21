
# calculate the power of a number


def pow(a,b):
    if b==0:
        return 1
    else:
        return a*pow(a,b-1)



def power(x,y):
    i=0
    p=1
    if y==0:
        return 1
    while i<y:
        p=p*x
        i+=1
    return p
