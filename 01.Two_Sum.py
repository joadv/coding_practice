class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        result = []
        twosum = 10000000000
        while count != len(nums):
            for i, n in enumerate(nums[count:]):
                if twosum == 10000000000:
                    twosum = n
                    result.append(i + count)
                else:
                    if (twosum + n) == target:
                        result.append(i + count)
                        return result

            count += 1
            result = []
            twosum = 10000000000