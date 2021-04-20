class Solution:
    def removeDuplicates(self,nums):
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast -1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

if __name__ == '__main__':
    a = Solution()
    b = [1,1,1,1,1,2,2,3,4,5,56]
    print(a.removeDuplicates(b))