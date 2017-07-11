class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        sum = 0
        while n != 0:
            n /= 5
            sum += n
        return sum

if __name__ == '__main__':
    print(Solution().trailingZeros(11))
