
alp = "abcdefghijklmnopqrstuvwxyz"


def next_letter(letter):
    if letter == "z":
        return "a"
    else:
        return alp[alp.find(letter)+1]

is_good = True

class GoodString:
    is_good = True
    @staticmethod
    def check_good(string, past_letter="~"):
        string = str(string)
        if len(string) == 1:
            return
        else:
            half = int(len(string)/2)
            left_s = string[0:half]
            right_s = string[half:len(string)]
            if left_s.count(left_s[0]) == len(left_s):

                new_letter = left_s[0]
                if past_letter != "~":

                    if new_letter == next_letter(past_letter):
                        GoodString.check_good(right_s, past_letter=new_letter)
                    else:
                        GoodString.is_good = False
                        return
                else:
                    GoodString.check_good(right_s, past_letter=new_letter)

            elif right_s.count(right_s[0]) == len(right_s):

                new_letter = right_s[0]
                if past_letter != "~":

                    if new_letter == next_letter(past_letter):
                        GoodString.check_good(left_s, past_letter=new_letter)
                    else:
                        GoodString.is_good = False
                        return
                else:
                    GoodString.check_good(left_s, past_letter=new_letter)

            else:
                GoodString.is_good = False
                return

GoodString.check_good("ffgheeee")
print(GoodString.is_good)
GoodString.check_good("aagheeee")
print(GoodString.is_good)
