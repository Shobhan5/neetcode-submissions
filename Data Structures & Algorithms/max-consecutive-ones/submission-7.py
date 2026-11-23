class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # =========================
        # max_count = 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         count = 0
        #         for j in range(i,len(nums)):
        #             if nums[j] == 1:
        #                 count += 1 
        #             else:
        #                 break 
        #         if count > max_count:
        #             max_count = count 
        # return max_count 
        # =============================
        # res, cnt = 0, 0 
        # for i in nums:
        #     if i == 1:
        #         cnt += 1 
        #     else:
        #         cnt = 0 
        #     res = max(res,cnt)
        # return res

        # ===========================

        res, cnt = 0,0 
        for i in nums:
            if i == 0:
                res = max(res, cnt)
                cnt = 0 
            else:
                cnt += 1 
        return max(res,cnt)



        