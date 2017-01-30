class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        table = {}

        for row in range(0, m):
            for col in range(0, n):
                if row == 0 or col == 0:
                    table[(row, col)] = 1
                else:
                    table[(row, col)] = table[
                        (row, col - 1)] + table[(row - 1, col)]
        return table[(m - 1, n - 1)]

if __name__ == '__main__':
    print(Solution().uniquePaths(4, 5))
