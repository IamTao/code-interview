class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here
        length = len(A)
        if length == 0:
            return False

        start, end = 0, length - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                return True
            if A[start] < A[mid]:
                if A[start] <= target and target < A[mid]:
                    end = mid
                else:
                    start = mid
            elif A[start] > A[mid]:
                if A[mid] < target and target <= A[end]:
                    start = mid
                else:
                    end = mid
            else:
                start += 1
        if A[start] == target or A[end] == target:
            return True
        else:
            return False
