class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers = sorted(numbers)
        results = {}

        for ind in range(len(numbers)):
            left, right = ind + 1, len(numbers) - 1

            while left < right:
                sum = numbers[ind] + numbers[left] + numbers[right]
                if sum == 0:
                    tmp = [numbers[ind], numbers[left], numbers[right]]
                    results["".join(map(str, tmp))] = tmp
                if sum < 0:
                    left += 1
                else:
                    right -= 1
        return results.values()

if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
