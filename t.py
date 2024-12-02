class Solution:
    def minKBitFlips(self, nums, k: int) -> int:
       n = len(nums)
       flips = 0
       i = 0 
       while i < n:
        if nums[i] == 1:
          i += 1
          continue
        if nums[i] == 0:
          flips += 1
          tmp = i
          first_zero = -1
          while i < tmp + k :
            if i >= n:
              return -1
            nums[i] = 1 - nums[i]
            if nums[i] == 0 and first_zero == -1:
              first_zero = i
            i += 1
          if first_zero != -1:
            i = first_zero
            
       print(nums)
       for i in range(n):
        if nums[i] != 1:
          return -1
       return flips


sol = Solution()
print(sol.minKBitFlips([1, 1, 0], 2))