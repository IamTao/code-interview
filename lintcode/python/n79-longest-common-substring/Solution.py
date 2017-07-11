class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        if A is None or B is None or A is "" or B is "":
            return 0

        len_of_A = len(A)
        len_of_B = len(B)

        C = [[0] * (len_of_B + 1) for _ in range(len_of_A + 1)]
        longest, a_longest = 0, 0
        for i in xrange(1, len_of_A + 1):
            for j in xrange(1, len_of_B + 1):
                if A[i - 1] == B[j - 1]:
                    C[i][j] = C[i - 1][j - 1] + 1
                    if C[i][j] > longest:
                        longest = C[i][j]
                        a_longest = i
                else:
                    C[i][j] = 0
        A[a_longest - longest: a_longest]
        return longest

if __name__ == '__main__':
    a = "www.lintcode.com code"
    b = "www.ninechapter.com code"

    Solution().longestCommonSubstring(a, b)
