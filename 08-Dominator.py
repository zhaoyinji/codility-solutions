def solution(A):
    N = len(A)
    
    # Let's find the value first
    size = 0
    
    for el in A:
        if size == 0:
            size += 1
            value = el
        else:
            if el != value:
                size -= 1
            else:
                size += 1
    
    index = -1
    count = 0
    
    for i,el in enumerate(A):
        if el == value:
            count += 1
            index = i
    
    if count > N/2:
        return index
    else:
        return -1