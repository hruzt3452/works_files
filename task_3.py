input_files = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'combined.txt'

separator = "=" * 40

try:
    with open(output_file, 'w', encoding='utf-8') as out_f:
        
        for filename in input_files:
            out_f.write(f"\n{separator}\n")
            out_f.write(f" НАЧАЛО ФАЙЛА: {filename}\n")
            out_f.write(f"{separator}\n")
            
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

except Exception as e:
    print("Ошибка!!", e)