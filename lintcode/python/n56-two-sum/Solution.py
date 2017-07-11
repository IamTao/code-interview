class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        numbers = sorted(enumerate(numbers), key=lambda x: x[1])
        len_numbers = len(numbers)

        left, right = 0, len_numbers - 1
        while left < right:
            sum = numbers[left][1] + numbers[right][1]
            if sum == target:
                l, r = numbers[left][0] + 1, numbers[right][0] + 1
                return [l, r] if l < r else [r, l]
            if sum < target:
                left += 1
            else:
                right -= 1
