def solution(A):
    max_count = 0

    if len(A) < 2:
        return len(A)

    A.sort()

    num1 = A[0]
    count1 = 1
    num2 = A[0] + 1
    count2 = 0

    for x in A[1:]:
        if x == num1:
            count1 += 1
            max_count = max(max_count, count1+count2)
            continue
        if x == num2:
            count2 += 1
            max_count = max(max_count, count1+count2)
            continue
        if x == num2 + 1:
            num1 = num2
            count1 = count2
            num2 = x
            count2 = 1
        else:
            num1 = x
            num2 = num1 + 1
            count1 = 1
            count2 = 0
        max_count = max(max_count, count1+count2)
    
    return max_count

assert solution([1]) == 1
assert solution([1, 1]) == 2
assert solution([1, 2, 1, 2, 5, 1, 5]) == 5
assert solution([1, 2, 1, 2, 3, 1, 3, 2, 3, 3]) == 7
