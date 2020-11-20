# class Solution(object):
#     def insert(self, intervals, newInterval):
        ###Method 1
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x[0])

        # res = []
        # for i in range(len(intervals)):
        #     if not res or intervals[i][0] > res[-1][1]:
        #         res.append(intervals[i])
        #     else:
        #         num = res.pop()
        #         end = max(num[1], intervals[i][1])
        #         res.append([num[0], end])

        # return res
import heapq
class Solution(object):
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: x[0])
        
        res = [intervals[0]]
        
        for x1, y1 in intervals[1:]:
            x0, y0 = res[-1]
            if y0 < x1:
                res.append([x1, y1])
            else:
                res[-1][0] = min(x1, x0)
                res[-1][1] = max(y0, y1)

        return res


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    result = Solution().insert(intervals, newInterval)
    print(result)

    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]
    # result = Solution().insert(intervals, newInterval)
    # print(result)

    # intervals = [[1, 5]]
    # ###newInterval = [2,3]
    # newInterval = [0, 3]
    # result = Solution().insert(intervals, newInterval)
    # print(result)
