def solution(numbers):
    num_array = [0] * 10001

    for num in numbers:
        num_array[int(num)] += 1

    for i in range(10001):
        if num_array[i] != 0:
            for j in range(num_array[i]):
                print(i)


print(solution('5231423517'))


