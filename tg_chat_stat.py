# coding=utf-8

import json
import chat_stat_lib as lib

# Path to file with data from Telegram
path_to_file = "C:/Users/Андрей/Downloads/Telegram Desktop/DataExport_11_01_2020(JSON)/result.json"

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
            print(key, chat_names[key]["name"])
        
        selected_chat = input("Введите номер чата для получения информации:\n-> ")
        selected_chat_number = chat_names[int(selected_chat)]["number"] # Выбранный номер чата, соответствующий номеру в файле
        selected_chat_dict = chat_list[selected_chat_number]["messages"] # Словарь сообщений выбраного чата

        lib.print_msg_count(chat_list[selected_chat_number]["name"], len(chat_list[selected_chat_number]["messages"]))
        print("Количество сообщений от " + user["first_name"] + " " + user["last_name"] + ":", lib.count_msg_from(user["user_id"], selected_chat_dict))
        print("Количество сообщений от " + chat_list[selected_chat_number]["name"] + ":", len(chat_list[selected_chat_number]["messages"]) - lib.count_msg_from(user["user_id"], selected_chat_dict))

    elif int(_input) == 0:
        is_active = False