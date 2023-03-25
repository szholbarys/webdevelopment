n = int(input())

arr = list(map(int, input().split()))[:n]

# arr = list(arr.reverse)

i = len(arr)-1

while(i>=0):
    print(arr[i], end=" ")
    i-=1