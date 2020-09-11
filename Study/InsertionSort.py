import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


random_arr = random.sample(range(100), 50)
print(insertion_sort(random_arr))


def insertion_sort2(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

    return arr


random_arr = random.sample(range(100), 50)
print(insertion_sort2(random_arr))
