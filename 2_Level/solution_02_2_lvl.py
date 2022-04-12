def solution(h, q):
    roots = []
    for i in range(len(q)):
        curr_num = 2 ** h - 1
        sub = 2 ** (h - 1)
        root = -1
        for j in range(h):
            if q[i] == curr_num:
                roots.append(root)
                break
            elif q[i] < (curr_num - sub + 1):
                root = curr_num
                curr_num -= sub
                sub = sub/2
            else:
                root = curr_num
                curr_num -= 1
                sub = sub/2
    return roots


sol = solution(5, [19, 14, 28])
print(sol)
