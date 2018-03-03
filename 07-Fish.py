def solution(A, B):
    N = len(A)
    
    saved = 0
    stack = []
    
    for i in range(N):
        if B[i] == 0:
            # downstream are potentially eaten
            while len(stack) > 0 and stack[-1] < A[i]:
                stack.pop()
            # if none remaining, one more is saved
            if len(stack) == 0:
                saved += 1
        else:
            stack.append(A[i])
    
    return saved + len(stack)