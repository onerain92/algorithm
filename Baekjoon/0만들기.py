import copy

def recursive(array, num):
    if len(array) == num:
        operators_list.append(copy.deepcopy(array))
        return

    array.append(' ')
    recursive(array, num)
    array.pop()

    array.append('+')
    recursive(array, num)
    array.pop()

    array.append('-')
    recursive(array, num)
    array.pop()


test_case = int(input())

for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([], n - 1)

    integers = [i for i in range(1, n + 1)]

    for operator in operators_list:
        string = ''
        for i in range(n - 1):
            string += str(integers[i]) + operator[i]
        string += str(integers[-1])

        if eval(string.replace(' ', '')) == 0:
            print(string)
