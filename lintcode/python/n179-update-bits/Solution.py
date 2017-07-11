class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here
        max_int = (2 ** 31) - 1
        min_int = - (2 ** 31)

        if j < 31:
            mask = ~ ((1 << (j + 1)) - (1 << i))
        else:
            mask = (1 << i) - 1

        result = (m << i) + (mask & n)
        return result % min_int if result > max_int else result
