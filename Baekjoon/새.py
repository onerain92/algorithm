def solution(birds):
    count = 0
    number_of_bird = 1

    while birds != 0:
        if number_of_bird >= birds:
            number_of_bird = 1
        birds -= number_of_bird
        number_of_bird += 1
        count += 1

    return count


print(solution(14))
