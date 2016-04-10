class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    @example:
        Given an array [0,4,4,0,0,2,4,4], value=4
        return 4 and front four elements of the array is [0,0,0,2]
    """
    def removeElement(self, A, elem):
        length = len(A)
        numNot = 0
        for i in range(length):
            if A[i] != elem:
                A[numNot] = A[i]
                numNot += 1
        return numNot

if __name__ == '__main__':
    assert Solution().removeElement([0,4,4,0,4,4,4,0,2], 4) == [0, 0, 0, 2]
