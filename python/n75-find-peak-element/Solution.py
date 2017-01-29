class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        length = len(A)
        if length < 3:
            return -1
        if length == 3:
            return 1

        start, end = 0, length - 1
        while start + 1 < end:
            mid = (start + end) / 2

            if A[mid + 1] > A[mid]:
                start = mid
            elif A[mid - 1] > A[mid]:
                end = mid
            else:
                return mid
        mid = start if A[start] > A[end] else end
        return mid

if __name__ == '__main__':
    print(Solution().findPeak([1, 2, 1, 3, 4, 5, 7, 6]))
    print(Solution().findPeak([1, 2, 4, 5, 6, 7, 8, 6]))
