def solution(money):
    count = 0
    change_list = [500, 100, 50, 10]

    for change in change_list:
        count += money // change
        money -= change * (money // change)

    return count


print(solution(5450))
