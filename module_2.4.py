numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i % 2 == 0 and i != 2 or i % 3 == 0 and i != 3 or i % 5 == 0 and i != 5:  #проверка на простоту
        not_primes.append(i)
    else:
        primes.append(i)
primes.remove(1)
print(not_primes)
print(primes)
