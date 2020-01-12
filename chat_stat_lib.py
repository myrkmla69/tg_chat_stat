# coding=utf-8

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

# Вывод корректного сообщения о количестве сообщений =)
def print_msg_count(name, count):
    str_count = str(count)
    str_count_last_index = len(str_count) - 1
    last_number = int(str_count[str_count_last_index])

    if last_number in range(2, 4):
        print(name, count, "сообщения")
    elif last_number in range(5, 9) or last_number == 0:
        print(name, count, "сообщений")
    elif last_number == 1:
        print(name, count, "сообщение")