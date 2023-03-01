# Leetcode 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

# solution 2 and 3 are essentially the same only that the helper function for 2 is defined inside the function

# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)

class Solution:
    def findKthLargest1(self, nums: list, k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
    
    def findKthLargest2(self, nums: list, k: int) -> int:
        k = len(nums) - k
        def quick_select(l, r):
            p = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if k < p:   return quick_select(l, p - 1)
            elif k > p: return quick_select(p + 1, r)
            else: return nums[p]
        
        return quick_select(0, len(nums) - 1)
    
    
    def partition(self, nums: list, left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest3(self, nums: list, k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

s = Solution()
ans = s.findKthLargest3(nums = [3,2,1,5,6,4], k = 2)
print(ans)