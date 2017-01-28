class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        result = 0
        for ind, val in enumerate(A):
            if ind == 0 or val >= A[ind - 1]:
                if result >= 2:
                    if A[result - 2] != val:
                        A[result] = val
                        result += 1
                else:
                    A[result] = val
                    result += 1
        return result
