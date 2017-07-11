class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        length = len(A)
        if length == 0:
            return [-1, -1]

        start, end = 0, length - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            left_bound = start
        elif A[end] == target:
            left_bound = end
        else:
            return [-1, -1]

        start, end = left_bound, length - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        right_bound = end if A[end] == target else start
        return [left_bound, right_bound]


if __name__ == '__main__':
    Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
