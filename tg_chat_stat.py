# coding=utf-8

import json
import chat_stat_lib as lib

# Path to file with data from Telegram
path_to_file = lib.get_path_to_file()

if path_to_file != "":
    with open(path_to_file, "r", encoding="utf8") as file:
        data = json.load(file)

    user = data["personal_information"] # Информация о пользователе (чей экспорт)
    print("Exported data of " + user["first_name"] + " " + user["last_name"] + " (" + user["username"] + ")" + " from Telegram successfully load!")

    chat_list = data["chats"]["list"] # Все данные чатов из файла
    chat_names = dict() # Список чатов
    counter = 0 # Счетчик чатов

    # Получаем названия чатов и заносим в другой список
    for i in range(0, len(chat_list) - 1):
        if chat_list[i]["type"] == "personal_chat": # Если это ЛС (диалог)
            counter += 1
            chat_names[counter] = {
                "number": i,
                "name": chat_list[i]["name"],
                "from_id": lib.get_from_id(chat_list[i]["name"], chat_list[i]["messages"])
            }

    is_running = True
    # Цикл работы программулины
    while is_running:
        
        print("\nВыберите действие:")
        print("1. Выбрать чат")
        print("0. Выход")

        _input = input("-> ")

        if int(_input) == 1:
            
            print("Список чатов:")
            for key in chat_names:
                print(str(key) + '.', chat_names[key]["name"] + f" (" + str(chat_names[key]["from_id"]) + ")")
            
            selected_chat = input("Введите номер чата для получения информации:\n-> ")

            selected_chat_number = chat_names[int(selected_chat)]["number"] # Выбранный номер чата, соответствующий номеру в файле
            selected_chat_dict = chat_list[selected_chat_number]["messages"] # Словарь сообщений выбраного чата
            selected_chat_count = len(chat_list[selected_chat_number]["messages"]) # Количество сообщений в чате
            selected_chat_popular_phrases = lib.get_phrases_count(selected_chat_dict) # Количество популярных фраз
            selected_chat_popular_marks = lib.get_marks_count(selected_chat_dict) # Количество знаков препинания
            

            print("\nСтатистика по выбранному чату (", chat_names[int(selected_chat)]["name"], "):\n")

            print("Всего сообщений:", "{:,}".format(selected_chat_count).replace(",", " "))
            print("Всего символов:", "{:,}".format(lib.count_chat_sybmols(selected_chat_dict)).replace(",", " "))
            print("Всего слов:", "{:,}".format(lib.count_msg_words(selected_chat_dict)).replace(",", " "))
            print("Всего голосовых сообщений:", "{:,}".format(lib.count_voice_msgs(selected_chat_dict)).replace(",", " "))
            print("Всего круглых-видео-сообщений:", "{:,}".format(lib.count_round_video_msgs(selected_chat_dict)).replace(",", " "))
            print("Всего ответов на сообщения (replies):", "{:,}".format(lib.count_msg_replies(selected_chat_dict)).replace(",", " ") + "\n")
            
            print("Среднее количество символов в сообщении:", "{:.0f}".format(lib.count_msg_avg_len(selected_chat_dict)))
            print("Среднее количество слов в сообщении:", "{:.0f}".format(lib.count_msg_avg_words(selected_chat_dict)))
            print("Среднее количество сообщений в день:", "{:.0f}".format(lib.count_avg_msgs_per_day(selected_chat_dict)) + "\n")

            print("Количество сообщений от " + user["first_name"] + " " + user["last_name"] + ":", "{:,}".format(lib.count_msg_from(user["user_id"], selected_chat_dict)).replace(",", " "))
            print("Количество сообщений от " + chat_list[selected_chat_number]["name"] + ":", "{:,}".format(selected_chat_count - lib.count_msg_from(user["user_id"], selected_chat_dict)).replace(",", " ") + "\n")

            print("Количество символов от " + user["first_name"] + " " + user["last_name"] + ":", "{:,}".format(lib.count_msg_symbols_from(user["user_id"], selected_chat_dict)).replace(",", " "))
            print("Количество символов от " + chat_list[selected_chat_number]["name"] + ":", "{:,}".format(lib.count_msg_symbols_from(chat_names[int(selected_chat)]["from_id"], selected_chat_dict)).replace(",", " ") + "\n")
            
            print("Количество слов от " + user["first_name"] + " " + user["last_name"] + ":", "{:,}".format(lib.count_msg_words_from(user["user_id"], selected_chat_dict)).replace(",", " "))
            print("Количество слов от " + chat_list[selected_chat_number]["name"] + ":", "{:,}".format(lib.count_msg_words_from(chat_names[int(selected_chat)]["from_id"], selected_chat_dict)).replace(",", " ") + "\n")

            print("Количество голосовых сообщений от " + user["first_name"] + " " + user["last_name"] + ":", "{:,}".format(lib.count_voice_msgs_from(user["user_id"], selected_chat_dict)).replace(",", " "))
            print("Количество голосовых сообщений от " + chat_list[selected_chat_number]["name"] + ":", "{:,}".format(lib.count_voice_msgs_from(chat_names[int(selected_chat)]["from_id"], selected_chat_dict)).replace(",", " ") + "\n")

            print("Количество круглых-видео-сообщений от " + user["first_name"] + " " + user["last_name"] + ":", "{:,}".format(lib.count_round_video_msgs_from(user["user_id"], selected_chat_dict)).replace(",", " "))
            print("Количество круглых-видео-сообщений от " + chat_list[selected_chat_number]["name"] + ":", "{:,}".format(lib.count_round_video_msgs_from(chat_names[int(selected_chat)]["from_id"], selected_chat_dict)).replace(",", " ") + "\n")
            
            print("Количество ответов на сообщения (replies) от " + user["first_name"] + " " + user["last_name"] + ":", "{:,}".format(lib.count_msg_replies_from(user["user_id"], selected_chat_dict)).replace(",", " "))
            print("Количество ответов на сообщения (replies) от " + chat_list[selected_chat_number]["name"] + ":", "{:,}".format(lib.count_msg_replies_from(chat_names[int(selected_chat)]["from_id"], selected_chat_dict)).replace(",", " ") + "\n")

            print("Популярные фразы:\n")
            for i in range(0, len(selected_chat_popular_phrases) - 1):
                print("\"" + selected_chat_popular_phrases[i]["phrase"] + "\":", "{:,}".format(selected_chat_popular_phrases[i]["count"]))

            print("\nКоличество знаков препинания:")
            for i in range(0, len(selected_chat_popular_marks) - 1):
                print("\"" + selected_chat_popular_marks[i]["mark"] + "\":", "{:,}".format(selected_chat_popular_marks[i]["count"]))

        elif int(_input) == 0:
            is_running = False
else:
    print("Экспортируйте данные из Telegram Desktop в формате JSON без дополнительных файлов (фото, видео, аудио и т.д.)")
    input('Press ENTER to exit\n')