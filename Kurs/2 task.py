
def task_2(s, value=0):
    if len(s)%2 == 1:
        if s.count(s[0]) == len(s):
            return 0
        else:
            return calculate(s)
    else:
        all_eq = True
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                all_eq = True
            else:
                all_eq = False
        if all_eq:
            return 0
        else:
            return calculate(s)


def calculate(s):
    s = str(s)
    counts_mas = []
    for i in range(len(s)):
        counts_mas.append(s.count(s[i]))
    max_counts = max(counts_mas)
    if max_counts>1:
        return len(s) - max_counts
    else:
        return len(s) - 2


def task2_tests(test_num, test_strings):
    results = []
    for i in range(test_num):
        results.append(task_2(test_strings[i]))
    return results


print(task2_tests(3,["95831","100120013","252525252525"]))
