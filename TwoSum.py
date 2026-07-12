class Solution:

    def twoSum(self, nums, target):
        numbers = {}

        for i in range(len(nums)):
            number = nums[i]
            nxt_num = target - number

            if nxt_num in numbers:
                return [numbers[nxt_num], i]

            numbers[number] = i