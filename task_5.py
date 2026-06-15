try:
    with open('resource/words.txt', 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]

    if len(words) == 0:
        print("Ошибка: Файл words.txt пуст!")
        exit()

    sorted_a = sorted(words)
    sorted_len = sorted(words, key=len)
    sorted_r = sorted(words, reverse=True)

    with open("resource/sorted_alphabetically.txt", 'w', encoding='utf-8') as f:
        for word in sorted_a:
            f.write(word + "\n")

    with open("resource/sorted_by_length.txt", 'w', encoding='utf-8') as f:
        for word in sorted_len:
            f.write(word + "\n")

    with open("resource/sorted_reverse.txt", 'w', encoding='utf-8') as f:
        for word in sorted_r:
            f.write(word + "\n")

    print("Готово!")

except FileNotFoundError:
    print("Ошибка!! Файл words.txt не найден!")
except Exception as e:
    print("Ошибка!!", e)