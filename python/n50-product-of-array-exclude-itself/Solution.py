class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        return self.productExcludeItself_1(A)

    def productExcludeItself_1(self, A):
        result = [1] * len(A)
        for ind in xrange(len(A) - 2, -1, -1):
            result[ind] = result[ind + 1] * A[ind + 1]
        left = 1
        for ind in xrange(len(A)):
            result[ind] *= left
            left *= A[ind]
        return result

    def productExcludeItself_2(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return A

        # scan from left to right
        l_product = [1]
        for ind in xrange(len(A)):
            l_product.append(l_product[ind] * A[ind])
        # scan from right to left
        r_product = [1]
        for ind in xrange(len(A) - 1, -1, -1):
            r_product.insert(0, r_product[0] * A[ind])
        # multiply
        return [l_product[ind] * r_product[ind + 1] for ind in xrange(len(A))]

if __name__ == '__main__':
    assert Solution().productExcludeItself([1, 2, 3]) == [6, 3, 2]
    assert Solution().productExcludeItself([0]) == [1]
