import collections

class Solution:
    def maxPoints(self, points) -> int:
        N = len(points)
        res = 0
        for i in range(N):
            lines = collections.defaultdict(int)
            duplicates = 1
            for j in range(i + 1, N):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    duplicates += 1
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                delta = self.gcd(dx, dy)
                lines[(dx / delta, dy / delta)] += 1
            res = max(res, (max(lines.values()) if lines else 0) + duplicates)
        return res
                
    # def gcd(self, x, y):
    #     return x if y == 0 else self.gcd(y, x % y)
    def gcd(self, x, y):
        if y == 0 :
            return x
        while y:
            x, y = y, x%y
        return x


if __name__ == '__main__':
    # points = [[1,1],[2,2],[3,3]]
    # res = Solution().maxPoints(points)
    # print(res)

    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    res = Solution().maxPoints(points)
    print(res)