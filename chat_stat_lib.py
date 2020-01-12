# coding=utf-8

import os

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
