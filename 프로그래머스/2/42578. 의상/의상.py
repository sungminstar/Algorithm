def solution(clothes):
    clothes_dic = {}

    for cloth, kind in clothes:
        if kind not in clothes_dic:
            clothes_dic[kind] = 0
        clothes_dic[kind] += 1

    combinations = 1
    for count in clothes_dic.values():
        combinations *= (count + 1)

    return combinations - 1
