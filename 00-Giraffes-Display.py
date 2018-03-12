def solution(A):
    group_max_stack = []
    group_max = A[0]
    for x in A:
        if x > group_max:
            group_max_stack.append(group_max)
            group_max = x
        else:
            while group_max_stack and x < group_max_stack[-1]:
                group_max_stack.pop()
    return len(group_max_stack) + 1 

assert solution([1, 2, 5, 4, 6, 7]) == 5
assert solution([1, 2, 5, 4, 6, 3]) == 3
assert solution([3, 2, 5, 4, 6, 1]) == 1
assert solution([2]) == 1
assert solution([1, 2, 5, 4, 7, 6, 10, 11, 12]) == 7