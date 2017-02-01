class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        if len(A) < k or not A:
            return ""
        stack = []
        count = 0

        for i in range(len(A)):
            current = A[i]
            while stack and stack[-1] > current and count < k:
                count += 1
                stack.pop()
            stack.append(current)

        while count < k:
            stack.pop()
            count += 1

        result = []
        while stack:
            result = [stack.pop()] + result

        while len(result) > 0 and result[0] == '0':
            result.pop(0)
        return ''.join(result)

    def DeleteDigits_1(self, A, k):
        # write you code here
        if len(A) < k or not A:
            return ""
        A = list(A)
        while k > 0:
            flag = True
            for i in range(len(A) - 1):
                if A[i] > A[i + 1]:
                    del A[i]
                    flag = False
                    break
            if flag and len(A) > 1:
                A.pop()
        while len(A) > 1 and A[0] == '0':
            del A[0]
        return ''.join(A)
