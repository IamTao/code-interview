class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 1
        n = len(A)

        for i in xrange(n):
            while (A[i] >= 1) and (A[i] <= n) and (A[i] != i + 1) and (A[i] != A[A[i] - 1]):
                tmp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = tmp

        for i in xrange(n):
            if A[i] != i + 1:
                return i + 1
        return n + 1
