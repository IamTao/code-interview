class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        # write your code here
        two = self.singleNumber(A)

        ind = 0
        x = 0
        while two:
            bit_element = (two >> ind) & 1
            if bit_element > 0:
                x = (bit_element << ind)
                break
            ind += 1

        b, c = [], []
        for num in A:
            if num & x > 0:
                b.append(num)
            else:
                c.append(num)
        return self.singleNumber(b), self.singleNumber(c)

    def singleNumber(self, A):
        # write your code here
        ans = 0
        for x in A:
            ans = ans ^ x
        return ans

    def singleNumberIII_2(self, A):
        # write your code here
        s = 0
        for x in A:
            s ^= x
        y = s & (-s)

        ans = [0, 0]
        for x in A:
            if (x & y) != 0:
                ans[0] ^= x
            else:
                ans[1] ^= x
        return ans


if __name__ == '__main__':
    print(Solution().singleNumberIII_2([1, 2, 3, 3, 2, 4, 1, 5]))
