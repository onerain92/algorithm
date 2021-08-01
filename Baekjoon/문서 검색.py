def solution(document, word):
    index = 0
    result = 0

    while len(document) - index >= len(word):
        if document[index:index + len(word)] == word:
            result += 1
            index += len(word)
        else:
            index += 1

    return result


print(solution('ababababa', 'aba'))
