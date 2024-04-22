word = str(input("Введите слово: "))
rare_sign = "ф"

for c in word:
    if c == rare_sign:
        print("Ого! Это редкое слово!")
        break
    
else:
    print("Эх, это не очень редкое слово...")