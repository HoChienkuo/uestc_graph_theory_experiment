import re


def validate_input(new_value):
    if new_value == "":
        return True  # 允许清空
    pattern = r'^\d+(,\d+)*,?$'
    return re.fullmatch(pattern, new_value) is not None


def str2seq(input_str: str):
    input_str = input_str.rstrip(",")
    split_arr = [s.strip() for s in input_str.split(',')]
    numbers = [int(p) for p in split_arr]
    return numbers


def is_graphical(degree_sequence):
    """
    判断一个度序列是否可图
    :param degree_sequence:
    :return:
    """
    seq = sorted(degree_sequence, reverse=True)
    while seq:
        d = seq.pop(0)
        if d < 0 or d > len(seq):
            return False
        for i in range(d):
            seq[i] -= 1
            if seq[i] < 0:
                return False
        seq.sort(reverse=True)
    return True
