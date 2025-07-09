class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        ans = []
        for xcenter, ycenter, r in queries:
            r2 = r**2
            cnt = 0
            for x, y in points:
                dx, dy = x - xcenter, y - ycenter
                if dx**2 + dy**2 <= r2:
                    cnt += 1
            ans.append(cnt)
        return ans