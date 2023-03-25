mkad = 109
velocity = int(input())
time = int(input())

s = velocity * time
d = s % mkad
print(d)
