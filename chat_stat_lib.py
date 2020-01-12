# coding=utf-8

import os
import re
import time

# Количество сообщений от пользователя (from_id)
def count_msg_from(from_id, msg_dict):
    msg_counter = 0
    
    for i in range(0, len(msg_dict) - 1):
        message = msg_dict[i]
        if message["from_id"] == from_id:
            msg_counter += 1

    return msg_counter

# Количество символов в сообщениях от пользователя (from_id)
def count_msg_symbols(from_id, msg_dict):
    pass 

# Получить from_id по имени (названию чата)
def get_from_id(name, msg_dict):
    pass

# Получение корректного сообщения о количестве сообщений =)
def get_msg_count(count):
    if count is None:
        return ""

    str_count = str(count)
    last_number = int(str_count[len(str_count) - 1])

    if last_number in range(2, 4):
        return "сообщения"
    elif last_number in range(5, 9) or last_number == 0:
        return "сообщений"
    elif last_number == 1:
        return "сообщение"


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def get_path_to_file():
    if os.name == "nt":
        tg_download_path = get_download_path() + "\Telegram Desktop" # Директория загрузок Telegram по-умолчанию
        tg_download_dirs = dict() # Список директорий
        tg_dir_count = 0 # Счетчик директорий

        if os.path.exists(tg_download_path): # Если данная директория существует
            for directory in os.listdir(tg_download_path): 
                if os.path.isdir(tg_download_path + "\\" + directory): # Отбираем только директории
                    if re.match("DataExport_+", directory): # Если это директории экспорта данных
                        if os.listdir(tg_download_path + "\\" + directory).count("result.json") == 1:
                            tg_dir_count += 1
                            tg_download_dirs[tg_dir_count] = directory # Добавляем в список

        print(f"Найдено файлов экспорта (json): {tg_dir_count}.")
        if tg_dir_count > 0:
            print("Выберите экспорт:")

            for i in range(1, tg_dir_count + 1):
                print(str(i) + ". " + tg_download_dirs[i])

            selected_export_file = int(input("-> "))
            
            if selected_export_file in range(1, tg_dir_count + 1):
                return tg_download_path + "\\" + tg_download_dirs[selected_export_file] + "\\result.json"
        else:
            return