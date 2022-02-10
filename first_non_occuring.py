# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


def solution(A):
    unique_array = set(A)
    m = max(unique_array)
    if m < 1:  # if the max is less than 1 then it should return 1 by default
        return 1
    if len(A) == 1:
        # if index 0 of A is 1, then 2 is the smallest possible int, otherwise, 1 is the smallest possible
        return 2 if A[0] == 1 else 1
    for i in range(1, m + 2):
        if i not in unique_array:
            return i


print(solution([1, 3, 4, 5, 6, 2]))
