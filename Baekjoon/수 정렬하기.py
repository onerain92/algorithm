import random

# 버블 정렬
def solution(numbers):
    for i in range(len(numbers) - 1):
        is_swap = False

        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                is_swap = True

        if is_swap == False:
            break

    return numbers


random_numbers = random.sample(range(100), 10)
print(solution(random_numbers))
