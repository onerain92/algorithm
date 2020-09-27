def solution(s):
    str_list = []
    total = 0

    for letter in s:
        if letter.isalpha():
            str_list.append(letter)
        else:
            total += int(letter)

    str_list.sort()
    return ''.join(str_list) + str(total)


print(solution('K1KA5CB7'))
print(solution('AJKDLSI412K4JSJ9D'))
