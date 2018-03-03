def solution(S):
    if len(S) == 0:
        return 1
    opening = ['{', '[','(']
    closing = ['}', ']',')']
    
    to_be_closed = []
    
    for c in S:
        if c in opening:
            i = opening.index(c)
            to_be_closed.append(closing[i])
        else:
            if len(to_be_closed) == 0:
                return 0
            if c != to_be_closed.pop():
                return 0
    
    if len(to_be_closed) == 0:
        return 1
    else:
        return 0