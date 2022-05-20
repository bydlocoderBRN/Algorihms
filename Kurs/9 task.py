def task_9(mas):
    sum = 0
    max_element = max(mas)
    for i in mas:
        sum+=i
    if sum%2 == 1 or max_element*2>sum:
        return False
    else:
        return True

print(task_9([6, 1, 2, 3, 4, 5, 6]))
