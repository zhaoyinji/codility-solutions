def solution(N):
    min_p = 2*1000000000 + 2

    i = 1
    while i*i < N:
        if N % i == 0:
            min_p = min(min_p, 2*(i + N//i))
        i += 1

    if i*i == N:
        return 4*i
        
    return min_p