a = int(input())

while(a>0):
    
    if(a==1):
        print("YES")
        break

    if a%2!=0:
        print("NO")
        break
    a = int(a/2)

