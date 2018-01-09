class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid - 1
            elif target >= nums[mid]:
                low = mid + 1
        return low


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 0))
