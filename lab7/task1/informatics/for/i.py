import math

x = int(input())

# Инициализируем переменную-счетчик
count = 0

# Используем цикл для перебора всех возможных делителей от 1 до sqrt(x)
for i in range(1, int(math.sqrt(x)) + 1):
    if x % i == 0:
        count += 1
        # Если делитель не равен корню из x, то добавляем еще один делитель x/i
        if i != x // i:
            count += 1

# Выводим количество делителей
print(count)
