# coding=utf-8

import os
import re

# Получить from_id по имени (названию чата)
def get_from_id(name, msg_dict):
    for i in range(0, len(msg_dict) - 1):
        if "from" in msg_dict[i]:
            if msg_dict[i]["from"] == name:
                return msg_dict[i]["from_id"]

# Количество сообщений от пользователя (from_id)
def count_msg_from(from_id, msg_dict):
    msg_counter = 0
    
    for i in range(0, len(msg_dict) - 1):
        if msg_dict[i]["from_id"] == from_id:
            msg_counter += 1

    return msg_counter

# Количество символов в чате
def count_chat_sybmols(msg_dict):
    symbols_count = 0
    for i in range(0, len(msg_dict) - 1):
        if msg_dict[i]["text"] != "":
            symbols_count += len(msg_dict[i]["text"])
    return symbols_count

# Количество символов в сообщениях от пользователя (from_id)
def count_msg_symbols_from(from_id, msg_dict):
    symbols_count = 0
    for i in range(0, len(msg_dict) - 1):
        if msg_dict[i]["text"] != "" and msg_dict[i]["from_id"] == from_id:
            symbols_count += len(msg_dict[i]["text"])
    return symbols_count

# Количество слов в чате
def count_msg_words(msg_dict):
    words_count = 0
    for i in range(0, len(msg_dict) - 1):
        if msg_dict[i]["text"] != "":
            word_list = str(msg_dict[i]["text"]).split()
            words_count += len(word_list)
    return words_count

# Количество слов в чате от пользователя (from_id)
def count_msg_words_from(from_id, msg_dict):
    words_count = 0
    for i in range(0, len(msg_dict) - 1):
        if msg_dict[i]["text"] != "" and msg_dict[i]["from_id"] == from_id:
            word_list = str(msg_dict[i]["text"]).split()
            words_count += len(word_list)
    return words_count

# Количество голосовых сообщений
def count_voice_msgs(msg_dict):
    audio_msg_count = 0
    for i in range(0, len(msg_dict) - 1):
        if "media_type" in msg_dict[i]:
            if msg_dict[i]["media_type"] == "voice_message":
                audio_msg_count += 1
    return audio_msg_count

# Количество голосовых сообщений
def count_voice_msgs_from(from_id, msg_dict):
    audio_msg_count = 0
    for i in range(0, len(msg_dict) - 1):
        if msg_dict[i]["from_id"] == from_id:
            if "media_type" in msg_dict[i]:
                if msg_dict[i]["media_type"] == "voice_message":
                    audio_msg_count += 1
    return audio_msg_count

# Количество видео-сообщений
def count_round_video_msgs(msg_dict):
    video_msg_count = 0
    for i in range(0, len(msg_dict) - 1):
        if "media_type" in msg_dict[i]:
            if msg_dict[i]["media_type"] == "video_message":
                video_msg_count += 1
    return video_msg_count

# Количество видео-сообщений от пользователя (from_id)
def count_round_video_msgs_from(from_id, msg_dict):
    video_msg_count = 0
    for i in range(0, len(msg_dict) - 1):
        if msg_dict[i]["from_id"] == from_id:
            if "media_type" in msg_dict[i]:
                if msg_dict[i]["media_type"] == "video_message":
                    video_msg_count += 1
    return video_msg_count

# Количество ответов на сообщения
def count_msg_replies(msg_dict):
    reply_count = 0
    for i in range(0, len(msg_dict) - 1):
        if "reply_to_message_id" in msg_dict[i]:
            reply_count += 1
    return reply_count

# Количество ответов на сообщения от пользователя (from_id)
def count_msg_replies_from(from_id, msg_dict):
    reply_count = 0
    for i in range(0, len(msg_dict) - 1):
        if "reply_to_message_id" in msg_dict[i] and msg_dict[i]["from_id"] == from_id:
            reply_count += 1
    return reply_count


# Количество популярных фраз
# def count_popular_phrases(msg_dict):
#     phrases_count = 0
#     popular_phrases = {
#        1: "ok",
#        2: "шо"
#     }
#     for i in range(0, len(msg_dict) - 1):

# Среднее количество символ в сообщении
def count_msg_avg_len(msg_dict):
    text_msg_count = 0
    symbols_count = 0
    for i in range(0, len(msg_dict) - 1):
        if msg_dict[i]["text"] != "":
            text_msg_count += 1
            symbols_count += len(msg_dict[i]["text"])
    return symbols_count / text_msg_count

# Среднее количество слов в сообщении
def count_msg_avg_words(msg_dict):
    text_msg_count = 0
    words_count = 0          
    for i in range(0, len(msg_dict) - 1):
        if msg_dict[i]["text"] != "":
            text_msg_count += 1
            words_count += len(str(msg_dict[i]["text"]).split())
    return words_count / text_msg_count

# Среднее количество сообщений в день
def count_avg_msgs_per_day(msg_dict):
    days_dict = dict()

    # Отбираем дни в словарь
    for i in range(0, len(msg_dict) - 1):
        curr_msg_date = str(msg_dict[i]["date"][0:10])
        if not curr_msg_date in days_dict:
            days_dict[curr_msg_date] = 0
    
    for i in range(0, len(msg_dict) - 1):
        curr_msg_date = str(msg_dict[i]["date"][0:10])
        if curr_msg_date in days_dict:
            days_dict[curr_msg_date] += 1

    return len(msg_dict) / len(days_dict)

# Путь к папке Загрузки текущего пользователя
def get_download_path():
    """Returns the default downloads path for Linux or Windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

# Путь к файлу экспорта Telegram (json)
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
            return ""
    else:
        print("Sorry, for now only Windows is currently supported")
        input('Press ENTER to exit\n')