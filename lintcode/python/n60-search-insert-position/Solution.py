class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        length = len(A)

        if length == 0:
            return 0

        start, end = 0, length - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if target <= A[start]:
            return min(0, start)
        elif target > A[end]:
            return end + 1
        else:
            return start + 1


if __name__ == '__main__':
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
    assert Solution().searchInsert([1, 3, 5, 6], 0) == 0
