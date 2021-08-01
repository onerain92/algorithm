N = int(input())
answer = 0

for i in range(1, N+1):
    splited_num = list(map(int, str(i)))
    answer = i + sum(splited_num)

    if answer == N:
        print(i)
        break

    if i == N:
        print(0)
