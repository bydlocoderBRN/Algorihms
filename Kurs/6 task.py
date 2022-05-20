def task_6(s, x):
    w = ['1']*len(s)
    for i in range(len(s)):
        if s[i] == "0":
            if 0 <= i-x <= len(s)-1:
                w[i-x] = 0
            if 0 <= i + x <= len(s) - 1:
                w[i+x] = 0
    return w

print(task_6("101110", 2))
