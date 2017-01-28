class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive_1(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 1
        n = len(A)

        for i in range(n):
            while (A[i] >= 1) and (A[i] <= n) and (A[i] != i + 1) and (A[i] != A[A[i] - 1]):
                tmp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = tmp

        for i in range(n):
            if A[i] != i + 1:
                return i + 1
        return n + 1

    def firstMissingPositive_2(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 1

        A = set(A)

        for ind in range(1, len(A) + 1):
            if ind not in A:
                return ind
        return len(A) + 1


if __name__ == '__main__':
    assert Solution().firstMissingPositive_2([1, 2, 0]) == 3
    assert Solution().firstMissingPositive_2([3, 4, -1, 1]) == 2
    assert Solution().firstMissingPositive_2([-1]) == 1
    assert Solution().firstMissingPositive_2([2, 2, 2, 2]) == 1
