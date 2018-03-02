# To avoid O(N^2), it is important to note that any average sum can be
# decomposed in average of 2 sums and 3 sums, and that an average of such
# combinations is greater or equal than one of its individual average
# Therefore we only need to compute such 2 and 3 sums average to find the minimum

def solution(A):
    min_idx = 0
    min_value = 10001
 
    for i in range(0, len(A)-1):
        if (A[i] + A[i+1])/2.0 < min_value:
            min_idx = i
            min_value = (A[i] + A[i+1])/2.0
        if i < len(A)-2 and (A[i] + A[i+1] + A[i+2])/3.0 < min_value:
            min_idx = i
            min_value = (A[i] + A[i+1] + A[i+2])/3.0
 
    return min_idx