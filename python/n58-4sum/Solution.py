class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of
              zero.
    """
    def fourSum(self, numbers, target):
        # write your code here
        len_num = len(numbers)
        numbers = sorted(numbers)
        results = []

        for i in range(len_num - 3):
            if i and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, len_num - 2):
                if j != i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                l, r = j + 1, len_num - 1
                while l < r:
                    sum = numbers[i] + numbers[j] + numbers[l] + numbers[r]
                    if sum == target:
                        results.append(
                            [numbers[i], numbers[j], numbers[l], numbers[r]])
                        r -= 1
                        l += 1
                        while l < r and numbers[l] == numbers[l - 1]:
                            l += 1
                        while l < r and numbers[r] == numbers[r + 1]:
                            r -= 1
                    if sum > target:
                        r -= 1
                    if sum < target:
                        l += 1
        return results

if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
