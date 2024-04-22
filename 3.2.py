# n = int(input("Введите количество слов: "))
i = "stop"
words=""
word=""
while word != "stop":
    word = str(input("Введите слово: "))
    if word == "stop":
            print(words)
            break
    words += word
    words += " "
#    i += 1
