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

    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str):
            left = 0
            right = len(s) - 1
            while left < right:
                leftc = s[left]
                rightc = s[right]
                if leftc != rightc:
                    return False
                left += 1
                right -= 1
            return True

        resp = []
        partition = []

        def dfs(idx: int):
            if idx >= len(s):
                resp.append(partition.copy())
                return
            for j in range(idx, len(s)):
                newstr = s[idx : j + 1]
                if is_palindrome(newstr):
                    partition.append(newstr)
                    dfs(j + 1)
                    partition.pop()

        dfs(0)
        return resp

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        res = []
        col = set()
        pos_diag = set()
        neg_diag = set()

        def dfs(r: int):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            #
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # backtrack
                dfs(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res
