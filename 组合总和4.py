'''
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。


'''
class Solution:
    def combinationsSum4(self,nums,target):
        dp = [1] + [0] * target  #dp = [1,0,0,0,0,0]
        for i in range(1,target+1):  #range(1,len+1)
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]

        return dp[target]



if __name__ == '__main__':
    a = Solution()
    nums = [1,2,3]
    target = 4
    print(a.combinationsSum4(nums, target))



