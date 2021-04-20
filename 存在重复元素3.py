'''给你一个整数数组 nums 和两个整数 k 和 t 。
请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def cns(self,nums,k,t):
        lens = len(nums)
        for i in range(lens):
            for j in range(lens):
                if i != j:
                    if abs(nums[i]-nums[j]) <= t and (i-j) <= k :
                        return True,i,j
                    elif abs(nums[j]-nums[i])<=t and j-i<=k :
                        return True,i,j
                    else:
                        return False
def s(nums):
    n=len(nums)
    for i in range(n):
        for j in range(n):

                print(j)



if __name__ == '__main__':
    a = Solution()
    nums = [1,2,3,1]
    k = 3
    t = 0
    # s(nums)
    print(a.cns(nums, k, t))