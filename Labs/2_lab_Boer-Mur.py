text = input("Строка: ")
sub_text = input("Подстрока: ")
button = input("Выбор опции чувствительности к регистрн -  on or off:  ")



def get_offset_table(sub_text):
    S = set()
    M = len(sub_text)
    dictionary = dict()
    for i in range(M - 2, -1, -1):
        if sub_text[i] not in S:
            dictionary[sub_text[i]] = M - i - 1
            S.add(sub_text[i])
    if sub_text[M - 1] not in S:
        dictionary[sub_text[M - 1]] = M
    dictionary['*'] = M
    return dictionary


def BM_algorithm(text, sub_text, button):
    if button == 'off':
        text = text.lower()
        sub_text = sub_text.lower()
    dictionary = get_offset_table(sub_text)
    str_len = len(text)
    substr_len = len(sub_text)
    if str_len >= substr_len:
        i = substr_len - 1
        while (i < str_len):
            k = 0
            j = 0
            flBreak = False
            for j in range(substr_len - 1, -1, -1):
                if text[i - k] != sub_text[j]:
                    if j == substr_len - 1:
                        if text[i] in dictionary:
                            off=dictionary[text[i]]
                        else:
                            off = dictionary['*']
                    else:
                        off = dictionary[sub_text[j]]
                    i += off
                    flBreak = True
                    break
                k += 1
            if not flBreak:
                return "Подстрока найдена"
        else:
            return "Подстрока не найдена"
    else:
        return "Подстрока не найдена"


print(BM_algorithm(text, sub_text, button))
