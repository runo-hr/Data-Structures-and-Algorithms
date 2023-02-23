class Solution:
    # O(nlog(n)) time
    def sortArray(self, nums: list) -> list:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[: mid]
        right = nums[mid:]
        
        self.sortArray(left)
        self.sortArray(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        return nums

s = Solution()
ans = s.sortArray([5,2,3,1])
print(ans) #2, 3, 5, 1
