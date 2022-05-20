def task8(t, n, a):
    for i in range(t):
        x = n[i]
        y = a[i].split(' ')
        cnt = [0 for j in range(x+1)]
        for j in range(x):
            cnt[int(y[j])] += 1
        ans = 0
        for j in range(x):
            summ = 0
            for k in range(j,x):
                summ += int(y[k])
                if j == k:
                    continue
                if summ <= x:
                    ans += cnt[summ]
                    cnt[summ] = 0
        print(ans)
t = 5
n = [9, 3, 5, 8, 1]
a = ["3 1 4 1 5 9 2 6 5", "1 1 2", "1 1 1 1 1", "8 7 6 5 4 3 2 1", "1"]
task8(t, n, a)