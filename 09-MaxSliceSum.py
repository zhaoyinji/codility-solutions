def solution(A):
    max_ending = max_slice = -1000000

    for el in enumerate(A):
        max_ending = max(el, max_ending+el)
        max_slice = max(max_slice, max_ending)
    
    return max_slice
