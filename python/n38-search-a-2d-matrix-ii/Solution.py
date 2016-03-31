class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
    	return self.searchMatrix1(matrix, target)

    def searchMatrix1(self, matrix, target):
    	count = 0
    	if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
    		return count
    	row = 0
    	col = len(matrix[0])
    	while row < len(matrix) and col > 0:
    		num = matrix[row][col - 1] 
    		if num  > target:
    			col -= 1
    		if num < target:
    			row += 1
    		if num == target:
    			count += 1
    			col -= 1
    	return count

    def searchMatrix2(self, matrix, target):
        # write your code here
		count 	= 0
		if len(matrix) > 0:
			col 	= len(matrix[0])
		else:
			return count
		num_row = len(matrix)
		for row in xrange(num_row):
			if len(matrix[row]) > 0 and matrix[row][0] > target:
				break
			for i in xrange(col):
				if matrix[row][i] > target:
					col = i
					break
				if matrix[row][i] == target:
					col = i
					count += 1
					break
		return count

if __name__ == '__main__':
	assert Solution().searchMatrix([[1, 3, 5, 7], [2, 4, 7, 8], [3, 5, 9, 10]], 3) == 2
	assert Solution().searchMatrix([[1, 3, 5, 7]], 3) == 1
	assert Solution().searchMatrix([[]], 3) == 0
	assert Solution().searchMatrix([], 3) == 0
	assert Solution().searchMatrix([[52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88],
									[53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89],
									[54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90],
									[55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91],
									[56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92],
									[57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93]], 71) == 3
