def fib(a):
    arr = [0, 1]

    i = 0
    while(i<a-2):
        x = arr[i]+ arr[i+1]
        arr.append(x)
        i+=1
    return arr
        


a = int(input())
print(fib(a))