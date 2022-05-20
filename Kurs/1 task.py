def task_1(n, s):
    inc = 0
    if n <= s:
        return 0
    else:
        while get_sum(n) > s:
            n += 1
            inc += 1
    return inc


def get_sum(value):
    str_val = str(value)
    sum = 0
    for i in range(len(str_val)):
        sum += int(str_val[i])
    return sum

print(task_1(500,4))