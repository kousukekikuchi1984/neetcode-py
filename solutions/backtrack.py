from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(cur: List[int], current_sum: int, position: int) -> bool:
            if current_sum == target:
                results.append(cur.copy())
                return
            if current_sum > target:
                return

            prev = -1
            for i in range(position, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                dfs(cur, current_sum + candidates[i], i + 1)
                cur.pop()
                prev = candidates[i]

        candidates.sort()
        dfs([], 0, 0)
        return results
