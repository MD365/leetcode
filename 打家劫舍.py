'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def rob(self,nums):
        if len(nums)==0:
            return nums[0]
        elif len(nums)==1:
            return max(nums)
        size = len(nums)
        dp = [0]*size
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range (2,size):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])

        return dp[size - 1]

    def rob1(self,nums):
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        first,second = nums[0],max(nums[0],nums[1])
        for i in range(2,size):
            first,second = second,max(first + nums[i],second)

        return second

if __name__ == '__main__':
    a = Solution()
    print(a.rob1([2, 7, 9, 3, 1]))