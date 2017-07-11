class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump_1(self, A):
        # write your code here
        import sys
        length = len(A)
        steps = [sys.maxint for ind in range(length)]
        steps[0] = 1

        for i in range(length):
            if steps[i] == sys.maxint:
                continue
            max_len = A[i]
            for j in range(max_len + 1):
                if i + j < length and steps[i + j] > steps[i] + 1:
                    steps[i + j] = steps[i] + 1
        return steps[-1]

    def jump_2(self, A):
        steps = [0]
        length = len(A)
        for ind in range(length - 1):
            while ind + A[ind] > len(steps) and len(steps) < len(A):
                steps.append(steps[ind] + 1)
        return steps[-1]

    def jump_3(self, A):
        start, end, jumps = 0, 0, 0
        length = len(A)
        while end < length - 1:
            jumps += 1
            farthest = end
            for i in range(start, end + 1):
                if A[i] + i > farthest:
                    farthest = A[i] + i
            start = end + 1
            end = farthest
        return jumps


if __name__ == '__main__':
    Solution().jump_3([13, 52, 42, 21, 58])
