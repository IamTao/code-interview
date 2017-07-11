class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        length = len(A)
        maps = [False for i in range(length)]
        maps[0] = True

        for i in range(length):
            if not maps[i]:
                continue
            current_max_jump = A[i]
            for j in range(current_max_jump + 1):
                if i + j < length:
                    maps[i + j] = True
        return maps[-1]

    def canJump_1(self, A):
        ans = 0
        for ind, item in enumerate(A[:-1]):
            ans = max(ans, ind + item)
            if ans <= ind:
                return False
        return True
