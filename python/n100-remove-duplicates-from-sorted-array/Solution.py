class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        len_of_A = len(A)
        result = 0

        for ind, val in enumerate(A):
            if ind == 0 or val > A[ind - 1]:
                A[result] = val
                result += 1
        return result

if __name__ == '__main__':
    Solution().removeDuplicates([-10,0,1,2,3])
