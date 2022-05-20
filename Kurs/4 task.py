def task4(mas):
    mas = list(mas)
    sorted_mas = mas.copy()
    sorted_mas.sort()

    mas_is_sorted = True
    for i in range(len(mas)):
        if mas[i] != sorted_mas[i]:
            mas_is_sorted = False
            break
    if mas_is_sorted:
        return 0
    else:
        has_eq_elements = False
        for i in range(len(mas)):
            if mas[i] == sorted_mas[i]:
                has_eq_elements = True
                break
        if has_eq_elements:
            return 2
        else:
            return 1

print(task4([3, 2, 4, 5, 1, 6, 7]))