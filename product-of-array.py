class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ons = [1]
        for i in range(1, len(nums)):
            ons.append(ons[-1] * nums[i - 1])
        cur = 1
        on=[1]
        for i in  nums[-2::-1]:
            cur *= i+1
            on.append(cur)
        on = on[::-1]
        for i in range(len(ons)):
            ons[i] *= on[i]
        
        return ons
o = Solution()
oo =o.productExceptSelf(nums=[1,2,3,4])
print(oo)