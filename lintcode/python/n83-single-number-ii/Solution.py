class Solution:
    """
	@param A : An integer array
	@return : An integer
    """
    def singleNumberII(self, A):
        # write your code here
        n = len(A)
        d = [0 for i in range(32)]
        for x in A:
            for j in range(32):
                if (((1 << j) & x) > 0):
                    d[j] += 1
        ans = 0
        for j in range(32):
            t = d[j] % 3
            if (t == 1):
                ans = ans + (1 << j)
            elif (t != 0):
                return -1
        return ans
