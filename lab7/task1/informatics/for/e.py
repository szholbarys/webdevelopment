x = int(input())
sum_digits = 0
while x > 0:
    sum_digits += x % 10
    x //= 10
print(sum_digits)
