def solution(key_input):
    answer = []
    temp = []

    for key in key_input:
        if key == '<':
            if answer:
                temp.append(answer.pop())
        elif key == '>':
            if temp:
                answer.append(temp.pop())
        elif key == '-':
            if answer:
                answer.pop()
        else:
            answer.append(key)

    for _ in range(len(temp)):
        answer.append(temp.pop())

    return ''.join(answer)


print(solution('<<BP<A>>Cd-'))
print(solution('ThIsIsS3Cr3t'))
print(solution('ABC<<D>E<<F>>--'))


def solution2():
    test_case = int(input())

    for _ in range(test_case):
        left_stack = []
        right_stack = []
        key_input = input()

        for key in key_input:
            if key == '-':
                if left_stack:
                    left_stack.pop()
            elif key == '<':
                if left_stack:
                    right_stack.append(left_stack.pop())
            elif key == '>':
                if right_stack:
                    left_stack.append(right_stack.pop())
            else:
                left_stack.append(key)

    left_stack.extend(reversed(right_stack))

    return ''.join(left_stack)


print(solution2())
