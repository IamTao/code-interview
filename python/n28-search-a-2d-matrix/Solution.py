class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        num_row = len(matrix)
        num_col = len(matrix[0])
        start = 0
        end = num_row * num_col - 1

        while end >= start:
            mid = (start + end) / 2
            row = mid / num_col
            col = mid % num_col

            if matrix[row][col] < target:
                start = mid + 1
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                return True
        return False

if __name__ == '__main__':
    test = [[1,4,8,15,20,22,25,32,36,43,49,51,53,55,59,65,69,73,80],[100,116,136,148,169,188,207,222,245,266,283,299,323,347,363,384,406,431,447],[460,477,494,512,532,548,562,582,604,617,630,643,663,675,690,713,735,758,783],[805,819,839,855,868,878,890,909,927,941,961,971,985,1000,1024,1037,1061,1086,1101],[1124,1135,1157,1182,1198,1221,1235,1254,1267,1277,1294,1319,1342,1361,1382,1400,1419,1440,1453],[1472,1495,1517,1542,1554,1567,1588,1603,1625,1642,1661,1680,1690,1702,1713,1725,1748,1771,1793]]
    assert Solution().searchMatrix(test, 81) == False
