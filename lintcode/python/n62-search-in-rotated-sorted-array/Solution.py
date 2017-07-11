class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        length = len(A)
        if length == 0:
            return -1

        start, end = 0, length - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            if A[start] < A[mid]:
                if A[start] <= target and target < A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] < target and target <= A[end]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1

if __name__ == '__main__':
    print(Solution().search([4, 5, 1, 2, 3], 1))
    print(Solution().search([4, 5, 1, 2, 3], 0))
    print(Solution().search([1, 2, 3], 1))
