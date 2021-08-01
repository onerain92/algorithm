def solution(record):
    result = []
    user_list = {}

    for message in record:
        if message.split(' ')[0] == 'Enter' or message.split(' ')[0] == 'Change':
            user_list[message.split(' ')[1]] = message.split(' ')[2]

    for message in record:
        if message.split(' ')[0] == 'Enter':
            result.append(user_list[message.split(' ')[1]] + '님이 들어왔습니다.')
        elif message.split(' ')[0] == 'Leave':
            result.append(user_list[message.split(' ')[1]] + '님이 나갔습니다.')

    return result


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
