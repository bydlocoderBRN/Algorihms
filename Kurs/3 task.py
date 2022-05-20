def task_3(length, code):
    pos0 =[]
    pos1 = []
    str_code = str(code)
    seq = Sequences()
    for i in range(len(str_code)):
        print(code[i])
        if code[i] == "0":
            seq.add_zero(i)
        elif code[i] == "1":
            seq.add_one(i)
    return seq.seq1


class Sequences:

    def __init__(self):
        self.seq0 = []
        self.seq1 = []

    def add_one(self, index):

        if self.seq1 == [] and self.seq0 == []:
            self.seq1.append([index])
        elif self.seq0 != []:
            tmp = self.seq0.pop()
            tmp.append(index)
            self.seq1.append(tmp)
        else:
            self.seq1.append([index])

    def add_zero(self, index):

        if self.seq1 == [] and self.seq0 == []:
            self.seq0.append([index])
        elif self.seq1 != []:
            tmp = self.seq1.pop()
            tmp.append(index)
            self.seq0.append(tmp)
        else:
            self.seq0.append([index])


def calculate_min_index(lists):
    lsts = [[]]
    lsts = lists
    lens = []
    for i in lsts:
        lens.append(len(i))
    min_len = min(lens)
    for i in range(len(lens)):
        if lens[i] == min_len:
            return i


print(task_3(1,"0011"))
