def solution(n, numbers):
    numbers = list(map(int, numbers))
    stack = []
    result = []
    numbers_index = 0

    for i in range(n):
        stack.append(i + 1)
        result.append('+')

        while stack and stack[-1] == numbers[numbers_index]:
            stack.pop()
            numbers_index += 1
            result.append('-')

    return '\n'.join(result) if not stack else 'NO'


print(solution(8, '43687521'))
print(solution(5, '12534'))


def solution2(n, number):
    count = 1
    stack = []
    result = []

    for i in range(1, n + 1):
        data = int(input())

        while count <= data:
            stack.append(count)
            count += 1
            result.append('+')

        if stack[-1] == data:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            break

    print('\n'.join(result))
