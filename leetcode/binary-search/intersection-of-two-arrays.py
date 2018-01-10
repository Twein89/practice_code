class Solution:
    def binary_search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return True
            elif target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1


    def intersection(self, nums1, nums2):
        nums2.sort()
        result = []
        for num in nums1:
            if self.binary_search(nums2, num) and num not in result:
                result.append(num)
        return result

if __name__ == '__main__':
    nums1 = [2, 1]
    nums2 = [1, 1]
    s = Solution()
    result = s.intersection(nums1, nums2)
    print(result)

