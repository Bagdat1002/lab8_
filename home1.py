def copy_line(source_file, destination_file, line_number):
    try:
        with open(source_file, 'r') as f_source:
            lines = f_source.readlines()
            if line_number < 1 or line_number > len(lines):
                print("Ошибка: Неверный номер строки.")
                return False
            line_to_copy = lines[line_number - 1]
        
        with open(destination_file, 'a') as f_dest:
            f_dest.write(line_to_copy)
        
        print(f"Строка номер {line_number} успешно скопирована в файл {destination_file}.")
        return True

    except FileNotFoundError:
        print("Один из файлов не найден.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

source_file = 'source.txt'
destination_file = 'destination.txt'

line_number = int(input("Введите номер строки для копирования: "))

if copy_line(source_file, destination_file, line_number):
    print("Завершено успешно.")
else:
    print("Не удалось.")
