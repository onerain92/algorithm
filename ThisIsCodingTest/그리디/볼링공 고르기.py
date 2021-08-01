from itertools import combinations

def solution(K):
    length = len(K)

    # 같은 무게의 볼링공 조합을 뺀 조합 리스트 구하기
    combination = [combi for combi in combinations(K, 2) if combi[0] != combi[1]]

    return len(combination)


print(solution([1, 3, 2, 3, 2]))
print(solution([1, 5, 4, 3, 2, 4, 5, 3]))



def solution2(K):
    n = len(K) # 볼링공의 갯수
    m = max(K) # 볼링공의 최대 무게

    array = [0] * 11 # 1부터 10까지의 무게를 담을 수 있는 리스트

    # 각 무게에 해당하는 볼링공의 개수 카운트
    for x in K:
        array[x] += 1

    result = 0

    # 1부터 m까지의 각 무게에 대하여 처리
    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n

    return result


print(solution([1, 3, 2, 3, 2]))
print(solution([1, 5, 4, 3, 2, 4, 5, 3]))
