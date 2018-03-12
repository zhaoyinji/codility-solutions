def solution(A):
    lasers = {}

    for x in A:
        if x[0] == 0:
            if x[1] > 0:
                lasers[float("inf")] = 1
            else:
                lasers[float("-inf")] = 1
        else:
            slope = x[1] / x[0]
            if slope in lasers:
                if x[0] > 0:
                    if lasers[slope] < 0:
                        lasers[slope] = 2
                else:
                    if lasers[slope] > 0:
                        lasers[slope] = 2
            else:
                if x[0] > 0:
                    lasers[slope] = 1
                else:
                    lasers[slope] = -1

    print(lasers)
    count = 0
    for i in lasers.keys():
        count += abs(lasers[i])

    return count

assert solution([(1,1), (-1,1), (-1,-1), (1,-1)]) == 4
assert solution([(3,1), (6,2)]) == 1
assert solution([(0,1), (1,1)]) == 2
assert solution([(0,1), (0,-2), (1,1)]) == 3
