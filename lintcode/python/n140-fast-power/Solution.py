class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if b == 0 or n < 0:
            return -1
        if b == 1:
            return 0
        if a == 1 or n == 0:
            return 1 % b
        if n == 1:
            return a % b

        product = self.fastPower(a, b, n / 2)
        product = (product * product) % b
        if n % 2 == 1:
            product = (product * (a % b)) % b
        return product
