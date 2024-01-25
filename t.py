class Solution:
    def numFactoredBinaryTrees(self, arr) -> int:
        arr.sort()
        dp = {}
        nums = {}
        for i in range(len(arr)):
            nums[arr[i]] = i

        for i in range(len(arr)):
            dp[i] = 1

        seen = set()

        def dfs(j):
            r = 0

            print(j)

            target = arr[j]

            for i in range(len(arr)):
                if i > j:
                    break
                if (arr[i], target // arr[i]) not in seen and target % arr[i] == 0 and (target // arr[i]) in nums:
                    k = nums[target // arr[i]]
                    r += dfs(i) + dfs(k)
                    seen.add((arr[i], target // arr[i]))

            dp[j] += r
            return dp[j]

        result = 0

        for i in range(len(arr)):
            result += dfs(i)

        return result


sol = Solution()

print('answer', sol.numFactoredBinaryTrees([2, 4]))
