n = int(input('Введите число от 3 до 20: '))
if n > 20 or n < 3:
    print('Число не может быть меньше 3 или больше 20')
else:
    password = ''
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i + j) == 0:
                password += f'{i}{j}'
    print(f'{n} - {password}')