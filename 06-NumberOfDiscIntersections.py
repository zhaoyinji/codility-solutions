# Every circle will define 2 points, one beginning, one end
# We will build a list of tuples (coord, isBeginning) and then by
# sorting them, we can count the intersection by checking the active
# number of circle at every step
def solution(A):
    points = []
    
    for i, a in enumerate(A):
        points += [(i-a, True), (i+a, False)]
    
    # we sort by index first, then begin points before end point for the same index
    # to account for the common point
    points.sort(key=lambda x: (x[0], not x[1]))
    
    active = 0
    result = 0
    
    for _, is_beginning in points:
        if is_beginning:
            result += active
            active += 1
        else:
            active -= 1
    
    if result > 10000000:
        return -1
    return result
