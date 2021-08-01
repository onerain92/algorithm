def solution(members):
    members.sort(key=lambda x: x[0])

    return members


print(solution([(21, 'Junkyu'), (21, 'Dohyun'), (20, 'Sunyoung')]))
