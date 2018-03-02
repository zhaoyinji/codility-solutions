def solution(A):
    found = {}
    
    for elt in A:
        found[elt] = True
    
    return len(found.keys())