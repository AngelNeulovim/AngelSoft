import subprocess
import os
from colorama import init, Fore
from colorama import init, Fore, Style
init(autoreset=True)
if not os.path.exists('base'):
    print(Fore.RED + "системе неудается найти папку 'base'.")
else:
    count = len(os.listdir('base'))
    data = input(Fore.GREEN + 'введите запрос: ')
    print(Fore.GREEN + '\nпоиск начат...\n')

    result = ''
    for label in os.listdir('base'):
        file_path = os.path.join('base', label)
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                for line in f:
                    if data in line:
                        result += f"[{label}] - {line}".replace('.', '').replace('[', '').replace(']', '').replace('"',
                                                                                                                   '').replace(
                            'NULL', '')
                        break
        except Exception as e:
            print(Fore.RED + f"Не найдено. По факту я не ебу, но пусть будет так.")

    # Вывод результатов поиска
    print(Fore.CYAN +'поиск окончен')
    if result:
        print(Fore.GREEN + '\nвот что мы нашли:\n')
        print(result)
    else:
        print(Fore.RED + "ничего не найдено.")

    f = input("нажмите enter... ': " + Style.RESET_ALL)
    if f == "":
        subprocess.run(["python", "main.py"])
