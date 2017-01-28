class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers = sorted(numbers)
        approx = None

        for ind in range(len(numbers)):
            left, right = ind + 1, len(numbers) - 1

            while left < right:
                sum = numbers[ind] + numbers[left] + numbers[right]
                if approx is None or abs(sum - target) < abs(approx - target):
                    approx = sum
                if sum < target:
                    left += 1
                else:
                    right -= 1
        return approx


if __name__ == '__main__':
    assert Solution().threeSumClosest([2, 7, 11, 15], 3) == 20
