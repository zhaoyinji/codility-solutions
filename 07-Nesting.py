def solution(S):
    if len(S) == 0:
        return 1
    o = '('
    c = ')'
    
    to_be_closed = 0
    
    for c in S:
        if c == o:
            to_be_closed += 1
        else:
            if to_be_closed == 0:
                return 0
            else:
                to_be_closed -= 1
    
    if to_be_closed == 0:
        return 1
    else:
        return 0