def solution(s):
    result = 0

    for letter in s:
        if result <= 1 or int(letter) <= 1:
            result += int(letter)
        else:
            result *= int(letter)

    return result


print(solution('02984'))
print(solution('567'))
