import random


def selection_sort(arr):
    length = len(arr)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


random_arr = random.sample(range(100), 50)
print(selection_sort(random_arr))
