input_files = ['resource/file1.txt', 'resource/file2.txt', 'resource/file3.txt']

try:
    with open('resource/combined.txt', 'w', encoding='utf-8') as out_f:
        
        for num, filename in enumerate(input_files, start=1):
            out_f.write(f"\n--- file{num} ---\n")
            
            try:
                with open(filename, 'r', encoding='utf-8') as in_f:
                    content = in_f.read()
                    out_f.write(content)
                    
                    if content and not content.endswith('\n'):
                        out_f.write('\n')
                        
            except FileNotFoundError:
                error_msg = f"[Ошибка!! Файл '{filename}' не найден!]\n"
                out_f.write(error_msg)
                print(f"Ошибка!! Файл '{filename}' не найден, пропускаем.")

    print("Файлы объединены в combined.txt")
    
except Exception as e:
    print("Ошибка!!", e)