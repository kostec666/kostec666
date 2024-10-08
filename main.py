
# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки
primes = []
not_primes = []

# Перебираем список numbers
for number in numbers:
    # Предполагаем, что число простое
    is_prime = True

    # Пропускаем 1, так как это не простое число
    if number == 1:
        is_prime = False

    # Вложенный цикл для проверки делителей
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print('Простые числа:', primes)
print('Не простые числа:', not_primes)





