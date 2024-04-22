import random

a = random.randint(1, 100)
b = random.randint(1, 100)
i = 0
t = 0

exercise = f'{a} + {b} = '

while i < 3:
    sum = int(input(exercise))
    if a + b != sum:
        i += 1
    else:
        t += 1
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    exercise = f'{a} + {b} = '
else:
    print("Игра окончена. Правильных ответов:", t)