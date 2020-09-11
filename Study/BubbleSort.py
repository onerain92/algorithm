import random

def bubble_sort(arr):
    length = len(arr) - 1

    for i in range(length):
        for j in range(length - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


random_arr = random.sample(range(100), 50)
print(bubble_sort(random_arr))
