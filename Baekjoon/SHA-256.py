# https://www.acmicpc.net/problem/10930
import hashlib


def solution(s):
    hash_object = hashlib.sha256()
    hash_object.update(s.encode())
    hex_dig = hash_object.hexdigest()

    return hex_dig

print(solution('Baekjoon'))
