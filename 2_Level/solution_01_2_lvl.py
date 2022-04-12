def solution(l):
    l.sort()
    rem = []
    number = 0
    for i in range(len(l)):
        rem.append(l[i] % 3)
    for i in range(2):
        sum_ = sum(rem)
        a = sum_ % 3
        if a != 0:
            if len(l) < 2:
                return number
            elif a not in rem:
                if a == 2:
                    for i in range(2):
                        ind = rem.index(1)
                        l.remove(l[ind])
                        rem.remove(rem[ind])
                else:
                    for i in range(2):
                        ind = rem.index(2)
                        l.remove(l[ind])
                        rem.remove(rem[ind])
            else:
                ind = rem.index(a)
                l.remove(l[ind])
                rem.remove(rem[ind])
        else:
            for i in range(len(l)):
                number += l[i] * (10 ** i)
            return number


sol = solution([3, 1, 4, 1, 5, 9])
print(sol)
