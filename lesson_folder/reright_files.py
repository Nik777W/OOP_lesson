# Программа для автоматической загрузки тестов из курса Поколение Python
# скачанные тесты программа берет из папки repr (переменная - directory)
# после запуска формируется файл(total.txt) для вставки в Unittest
# во время прохождения теста создается 1 файл (можно удалять) необходимый для
# сверки результатов, так как ответы даны в отдельном файле

import os


def get_file_names(folder_start):
    return [entry for entry in os.listdir(folder_start) if os.path.isfile(os.path.join(folder_start, entry))]


directory = "/Users/evgenii/Documents/Project_python/OOP_corses/repr"
output_file = 'total.txt'

file_names = get_file_names(directory)
file_names = filter(lambda x: not x.endswith(('clue', '.DS_Store')), file_names)

with open(output_file, 'w', encoding='utf-8') as total_file:
    for i in sorted(file_names, key=int):
        file_path = os.path.join(directory, i)
        clue_path = os.path.join(directory, f"{i}.clue")


        with open(file_path, 'r', encoding='utf-8') as file_test:
            with open(clue_path, 'r', encoding='utf-8') as clue:
                list_folders = [
                    f"{' ' * 8}{i.rstrip()[:-1]}, file=fil)" if 'print(' in i else f'{' ' * 8}{i.rstrip()}' for i in
                    list(file_test) if i != '\n']

                flag = False
                if 'end=' in list_folders[-1]:
                    flag = True
                ms = list(clue)
                if not flag:
                    ms[-1] = f'{ms[-1]}\n'              #   добавляем перенос строки к ответу




        print(f'{' ' * 4}def test_{i}(self):', file=total_file)
        print(f"{' ' * 8}fil = open('temp_for_right_files.txt', 'w', encoding='utf-8')", file=total_file)
        print(*list_folders, sep='\n', file=total_file)
        print(f'{' ' * 8}fil.close()', file=total_file)
        print(f"{' ' * 8}with open('temp_for_right_files.txt', 'r', encoding='utf-8') as papa_file:", file=total_file)
        print(f'{' ' * 12}self.assertEqual(list(papa_file) == {ms}, True)', file=total_file)
        print('', file=total_file)
