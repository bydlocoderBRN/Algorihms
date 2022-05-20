def task_7(n):
    n = list(n)
    n.sort(reverse=True)
    count = 0
    health = 0
    for i in range(len(n)):
        tmp = n.pop(0)
        if health + tmp >=0:
            health += tmp
            count+=1
    return count

print(task_7([4, -4, 1, -3, 1, -3]))