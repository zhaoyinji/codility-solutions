def solution(A):
    N = len(A)
    
    # compute the leader and its number of occurence
    size = 0

    for el in A:
        if size == 0:
            size += 1
            value = el
        else:
            if el == value:
                size += 1
            else:
                size -= 1

    total = 0
    for el in A:
        if el == value:
            total += 1
            
    count = 0
    equi = 0
    for i,el in enumerate(A):
        if el == value:
            count += 1
        if count > (i+1)/2 and total-count>(N-i-1)/2:
            equi += 1
    
    return equi
    