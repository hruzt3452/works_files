search_word = input("Введите слово для поиска: ").strip().lower()

total_count = 0     
line_numbers = []     

try:
    with open('resource/text.txt', 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            
            words = [word.strip('.,!?;:"\'()') for word in line.split()]
            
            words_lower = [word.lower() for word in words]
            
            count_in_line = words_lower.count(search_word)
            
            if count_in_line > 0:
                total_count += count_in_line
                line_numbers.append(line_num)

    if total_count > 0:
        print("\nСЛОВО НАЙДЕНО")
        print(f"Количество встреч: {total_count}")
        print(f"Номера строк: {', '.join(map(str, line_numbers))}")
    else:
        print("\nСЛОВО НЕ НАЙДЕНО")
        print(f"Количество встреч: 0")
        print(f"Номера строк: -")

    with open('resource/search_results.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(f"Искомое слово: {search_word}\n")
        f_out.write(f"Найдено: {'Да' if total_count > 0 else 'Нет'}\n")
        f_out.write(f"Общее количество: {total_count}\n")
        f_out.write(f"Номера строк: {line_numbers}\n")
    

except FileNotFoundError:
    print("Ошибка!! Файл 'text.txt' не найден!")
except Exception as e:
    print("Ошибка!!", e)