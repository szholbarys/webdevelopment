from math import sqrt

a = int(input())
i=1

while i<=a:
    sqr = int(sqrt(i))
    if(sqr*sqr==i):
        print(i)
    i+=1