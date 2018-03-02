def solution(A):
    N = len(A)
    
    if N < 3:
        return 0
    
    A.sort()
    
    for i in range(N-2):
        P = A[i]
        Q = A[i+1]
        R = A[i+2]
        if P+Q>R and Q+R>P and R+P>Q:
            return 1
    
    return 0