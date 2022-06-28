import os
def korean_number(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    return switcher.get(argument, "not within parameters")

if __name__ == "__main__":
    argument = 0
    print (korean_number(10))
