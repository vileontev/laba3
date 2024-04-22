n = int(input("Введите количество слов: "))
i = 0
word=""
while i < n:
    word += str(input("Введите слово: "))
    word += " "
    i += 1
else:
    print(word)