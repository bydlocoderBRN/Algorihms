# Пример использования стека типа LIFO

class Stack:

    def __init__(self, data=None):
        if data is None:
            self.stack = []
        else:
            self.stack = data

    def isEmpty(self):
        return self.stack == []

    def append(self, obj):
        tmpstack = self.stack + [None]
        tmpstack[len(self.stack)]=obj
        self.stack = tmpstack

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            obj = self.stack[len(self.stack)-1]
            tmpstack = self.stack[:len(self.stack)-1]
            self.stack=tmpstack
            return obj

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def __repr__(self):
        return self.stack


class Deque:
    def __init__(self, data=None):
        if data is None:
            self.items = []
        else:
            self.items = data

    def isEmpty(self):
        return self.items == []

    def pushLeft(self, item):
        self.items.insert(0, item)

    def pushRight(self, item):
        self.items.append(item)

    def popLeft(self):
        return self.items.pop(0)

    def popRight(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def stack_bracket():
    a = input("Введите строку: ")
    stack = Stack()
    flVerify = True

    for lt in a:
        if lt in "([{":
            stack.append(lt)
        elif lt in ")]}":
            if len(stack) == 0:
                flVerify = False
                break

            br = stack.pop()
            if br == '(' and lt == ')':
                continue
            if br == '[' and lt == ']':
                continue
            if br == '{' and lt == '}':
                continue

            flVerify = False
            break

    if flVerify and len(stack) == 0:    # стек по итогам проверок должен быть пустым
        print("Yes")
    else:
        print("No")


def deq_bracket():
    text = input("Введите строку: ")
    deq = Deque()

    for i in text:
        if i in '[({})]':
            deq.pushLeft(i)

    brac_is_ok = True

    if len(deq)%2 !=0:
        brac_is_ok = False
    else:

        while not deq.isEmpty():
            left = deq.popLeft()
            right = deq.popRight()
            if left == '(' and  right == ')':
                continue
            elif left == '[' and right == ']':
                continue
            elif left == '{' and right == '}':
                continue
            else:
                brac_is_ok = False
                break

    if brac_is_ok:
        print('Yes')
    else:
        print('No')




def abcSort(strings):
    deq1 = Deque(strings)
    deq2 = Deque()
    deq2.pushRight(deq1.popRight())
    while not deq1.isEmpty():
        tmp1 = deq1.popRight()
        tmp2 = deq2.popRight()
        if tmp1 >= tmp2:
            deq2.pushRight(tmp2)
            deq2.pushRight(tmp1)
        elif tmp1 <= tmp2:
            deq2.pushRight(tmp2)
            tmp2 = deq2.popLeft()
            if tmp1 <= tmp2:
                deq2.pushLeft(tmp2)
                deq2.pushLeft(tmp1)
            else:
                deq2.pushLeft(tmp2)
                tmp2 = deq2.popRight()
                replace_count=0
                while tmp1 < tmp2:
                    deq1.pushRight(tmp2)
                    tmp2 = deq2.popRight()
                    replace_count += replace_count
                deq2.pushRight(tmp2)
                deq2.pushRight(tmp1)
                for i in range(replace_count+1):
                    deq2.pushRight(deq1.popRight())
    return deq2.items + deq1.items


print(abcSort(["qwe","gfd","bvc","kjh","asd","oiu","fgh","lkh","vbn"]))

def decode(data, code):
    deq = Deque()
    for i in code:
        deq.pushRight(i)

    result = ""
    for el in data:
        temp_stack = Stack()
        temp = deq.popLeft()
        i = 1
        while el != temp:
            temp_stack.append(temp)
            temp = deq.popLeft()
        if temp_stack.isEmpty():
            deq.pushLeft(temp)
            temp_stack.append(deq.popRight())
            temp = deq.popRight()
            result += temp
            deq.pushRight(temp)
            deq.pushRight(temp_stack.pop())
        elif len(temp_stack.stack) == 1:
            deq.pushLeft(temp)
            deq.pushLeft(temp_stack.pop())
            temp = deq.popRight()
            result += temp
            deq.pushRight(temp)
        else:
            deq.pushLeft(temp)
            temp2 = temp_stack.pop()
            temp = temp_stack.pop()
            result += temp
            deq.pushLeft(temp2)
            deq.pushLeft(temp)
            while temp_stack.isEmpty() is False:
                deq.pushLeft(temp_stack.pop())
    return result


print(decode("сткджф","абвгдеёжзийклмнопрстуфхцчшщъыьэюя"))


class Pyramid:

    rods= {1: Stack(), 2: Stack(), 3: Stack()}

    @staticmethod
    def func(cls, data):
        cls.rods[1] = Stack(data)
        cls.solve(Pyramid, len(cls.rods[1].stack), 1, 3)
        return cls.rods[3]

    @staticmethod
    def solve(cls, n, i, k):
        if n == 1:
            print(f"Переложить из {i} в {k}")
            cls.rods[k].append(cls.rods[i].pop())
        else:
            cls.solve(Pyramid, n - 1, i, 6 - i - k)
            print(f"Переложить из {i} в {k}")
            cls.rods[k].append(cls.rods[i].pop())
            cls.solve(Pyramid, n - 1, 6 - i - k, k)


print(Pyramid.func(Pyramid,[423,6542,2,45,543,3,765]))


def symbols(data):
    numbers = Stack()
    letters = Stack()
    others = Stack()
    for i in data:
        if i.isdigit():
            numbers.append(i)
        elif i.isalpha():
            letters.append(i)
        else:
            others.append(i)

    result =""

    while not numbers.isEmpty():
        result += str(numbers.pop())

    while not letters.isEmpty():
        result += str(letters.pop())

    while not others.isEmpty():
        result += str(others.pop())
    return result


print(symbols('# print(abcSort(["123","435","654","kjh","asd","oiu","fgh","lkh","vbn"]))'))


def plus_minus(data):
    deq = Deque()
    for i in data:
        if i>=0:
            deq.pushRight(i)
        else:
            deq.pushLeft(i)
    return deq


print(plus_minus([1,-1,2,-5,4,-7,6,-8]))


def reverse_str(data):
    strings = data.split('\n')
    stack = Stack()
    for i in strings:
        stack.append(i)
    result = ""
    while not stack.isEmpty():
        result += stack.pop()+'\n'
    return result


print(reverse_str("first str\nsecond str\nthird str"))
