class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        while m != 0 or n != 0:
            if n == 0:
                A[m + n - 1] = A[m - 1]
                m -= 1
            elif m == 0:
                A[m + n - 1] = B[n - 1]
                n -= 1
            elif A[m - 1] > B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m -= 1
            else:
                A[m + n - 1] = B[n - 1]
                n -= 1

if __name__ == '__main__':
    print Solution().mergeSortedArray([1, 2, 3, None, None], 3, [4, 5], 2)
    print Solution().mergeSortedArray([1, 2, 7, None, None], 3, [4, 5], 2)
    print Solution().mergeSortedArray([9, 10, 11, 12, 13], 5, [4, 5, 6, 7], 4)
