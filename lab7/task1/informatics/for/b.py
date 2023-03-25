a = int(input())
b = int(input())
c = int(input())
d = int(input())

found = False
for i in range(a, b + 1):
    if i % d == c:
        print(i, end=' ')
        found = True
if not found:
    pass  
