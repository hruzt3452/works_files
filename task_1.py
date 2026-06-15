try:
    with open('resource/input.txt', "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)

    total_words = 0
    for line in lines:
        words = line.split()          
        total_words += len(words)     

    with open('resource/statistics.txt', "w", encoding="utf-8") as f:
        f.write(f"Строк: {total_lines}\n")
        f.write(f"Слов: {total_words}\n")

    print("Строк:", total_lines)
    print("Слов:", total_words)

except FileNotFoundError:
    print("Ошибка!! Файл input.txt не найден!")
except Exception as e:
    print("Ошибка!!", e)
