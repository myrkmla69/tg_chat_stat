# coding=utf-8

import os
import re
import json
import time
import chat_stat_lib as lib

# Path to file with data from Telegram
path_to_file = "C:/Users/Андрей/Downloads/Telegram Desktop/DataExport_12_01_2020/result.json"

if os.name == "nt":
    tg_download_path = lib.get_download_path() + "\Telegram Desktop" # Директория загрузок Telegram по-умолчанию
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
    print("Выберите экспорт:")

    for i in range(1, tg_dir_count + 1):
        print(str(i) + ". " + tg_download_dirs[i])

    selected_export_file = int(input("-> "))

    if selected_export_file in range(1, tg_dir_count):
        path_to_file = tg_download_path + "\\" + tg_download_dirs[selected_export_file] + "\\result.json"

with open(path_to_file, "r", encoding="utf8") as file:
    data = json.load(file)

user = data["personal_information"] # Информация о пользователе (чей экспорт)
print("Exported data of " + user["first_name"] + " " + user["last_name"] + " (" + user["username"] + ")" + " from Telegram successfully load!")

chat_list = data["chats"]["list"] # Все данные чатов из файла
chat_names = dict() # Список чатов
counter = 0 # Счетчик чатов

for i in range(0, len(chat_list) - 1):
    if chat_list[i]["type"] == "personal_chat": # Если это ЛС (диалог)
        counter += 1
        chat_names[counter] = {
            "number": i,
            "name": chat_list[i]["name"] # Получаем названия чатов и заносим в другой список
        }

is_active = True
# Цикл работы программулины
while is_active:
    
    print("\nВыберите действие:")
    print("1. Выбрать чат")
    print("0. Выход")

    _input = input("-> ")

    if int(_input) == 1:
        
        print("Список чатов:")
        for key in chat_names:
            print(str(key) + '.', chat_names[key]["name"])
        
        selected_chat = input("Введите номер чата для получения информации:\n-> ")

        selected_chat_number = chat_names[int(selected_chat)]["number"] # Выбранный номер чата, соответствующий номеру в файле
        selected_chat_dict = chat_list[selected_chat_number]["messages"] # Словарь сообщений выбраного чата
        selected_chat_count = len(chat_list[selected_chat_number]["messages"])

        print("\nСтатистика по выбранному чату (", chat_names[int(selected_chat)]["name"], "):\n")
        print("Всего", selected_chat_count, lib.get_msg_count(selected_chat_count))
        print("Количество сообщений от " + user["first_name"] + " " + user["last_name"] + ":", lib.count_msg_from(user["user_id"], selected_chat_dict))
        print("Количество сообщений от " + chat_list[selected_chat_number]["name"] + ":", selected_chat_count - lib.count_msg_from(user["user_id"], selected_chat_dict))

    elif int(_input) == 0:
        is_active = False