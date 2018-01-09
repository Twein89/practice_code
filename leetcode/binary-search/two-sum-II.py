class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(numbers):
            low, high = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while low <= high:
                mid = (low + high) // 2
                if(tmp == numbers[mid]):
                    return [i + 1, mid + 1]
                elif(tmp <= numbers[mid]):
                    high = mid - 1
                else:
                    low = mid + 1



if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([1,2,3,7,9], 9))

