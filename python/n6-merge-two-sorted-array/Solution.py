class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        C = []
        len_A = len(A)
        len_B = len(B)
        p_a, p_b = 0, 0

        if len_A == 0 and len_B != 0:
            return B
        if len_A != 0 and len_B == 0:
            return A

        while (p_a != len_A) or (p_b != len_B):
            if p_a == len_A:
                return C + B[p_b:]
            if p_b == len_B:
                return C + A[p_a:]
            if A[p_a] > B[p_b]:
                C.append(B[p_b])
                p_b += 1
            else:
                C.append(A[p_a])
                p_a += 1
        return C

if __name__ == '__main__':
    Solution().mergeSortedArray(
        [1, 2, 3, 4], [2, 4, 5, 6]) == [1, 2, 2, 3, 4, 4, 5, 6]
    Solution().mergeSortedArray([1], [1]) == [1, 1]
