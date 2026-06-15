def shift(text, n):
    result = ""
    for c in text:
        if c.isalpha():
            if c.isupper():
                result += chr((ord(c) - 65 + n) % 26 + 65)
            else:
                result += chr((ord(c) - 97 + n) % 26 + 97)
        else:
            result += c
    return result


try:
    with open('resource/secret.txt', "r", encoding="utf-8") as f:
        text = f.read()

    encrypted = shift(text, 3)
    decrypted = shift(encrypted, -3)

    with open('resource/encrypted.txt', "w", encoding="utf-8") as f:
        f.write(encrypted)

    with open('resource/decrypted.txt', "w", encoding="utf-8") as f:
        f.write(decrypted)

    print("Зашифровано в encrypted.txt")
    print("Расшифровано в decrypted.txt")

except FileNotFoundError:
    print("Ошибка!! Файл secret.txt не найден!")
except Exception as e:
    print("Ошибка!!", e)