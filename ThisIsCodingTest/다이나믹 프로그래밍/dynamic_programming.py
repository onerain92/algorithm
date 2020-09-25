# 메모이제이션 기법 활용
# 피보나치 수열 ( 재귀적 )
d = [0] * 100


def recursive_fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = recursive_fibo(x - 1) + recursive_fibo(x - 2)
    return d[x]


print(recursive_fibo(99))

# 피보나치 수열 ( 반복 )

arr = [0] * 100

def loop_fibo(n):
    arr[1] = 1
    arr[2] = 1

    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


print(loop_fibo(99))
