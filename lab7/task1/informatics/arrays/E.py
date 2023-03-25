n = int(input())

arr = list(map(int, input().split()))[:n]

for i in range(len(arr-1)):
    if(i==0):
        if(arr[i]==arr[i+1]):
            print("YES")
            break 
    elif(i == len(arr)-1):
        if(arr[i]==arr[i+1]):
            print("YES")
        else:print("NO")
    else:
        if arr[i-1] == arr[i] or arr[i]==arr[i+1]:
            print("YES")
            break
    