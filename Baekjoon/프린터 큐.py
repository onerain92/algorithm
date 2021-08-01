def solution():
    test_case = int(input())

    for _ in range(test_case):
        number_of_doc, target_doc = list(map(int, input().split(' ')))
        queue = list(map(int, input().split(' ')))
        queue = [(idx, priority) for idx, priority in enumerate(queue)]
        count = 0

        while queue:
            highest_priority = max(queue, key=lambda x: x[1])[1]
            current_idx, current_priority = queue.pop(0)
            if highest_priority == current_priority:
                count += 1
                if current_idx == target_doc:
                    print(count)
                    break
            else:
                queue.append((current_idx, current_priority))


solution()


def solution2():
    test_case = int(input())

    for _ in range(test_case):
        n, m = list(map(int, input().split(' ')))
        queue = list(map(int, input().split(' ')))
        queue = [(i, idx) for idx, i in enumerate(queue)]

        count = 0
        while True:
            if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
                count += 1

                if queue[0][1] == m:
                    print(count)
                    break
                else:
                    queue.pop(0)
            else:
                queue.append(queue.pop(0))
