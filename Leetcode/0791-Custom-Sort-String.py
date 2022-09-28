from collections import defaultdict
import collections

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        pos = collections.defaultdict(int)
        for i in range(len(S)):
            pos[S[i]] = i
        res = sorted(T, key = lambda x: pos[x])
        return "".join(res)


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = dict(zip(order, range(len(order))))
        m = defaultdict(list)
        for i in range(len(s)):
            if s[i] in d:
                m[d[s[i]]].append(s[i])
            else:
                m[len(d)].append(s[i])
        m = sorted(m.items(), key=lambda x: x[0])
        res = ''
        for k, v in m:
            res += ''.join(v)
        return res


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = collections.Counter(s)
        res = []

        # Write all characters that occur in S, in the order of S.
        for c in order:
            res.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0

        # Write all remaining characters that don't occur in S.
        # That information is specified by 'count'.
        for c in count:
            res.append(c * count[c])

        return "".join(res)

if __name__ == "__main__":
    res = Solution().customSortString(order = "cba", s = "abcd")
    print(res)

    res = Solution().customSortString(order = "cbafg", s = "abcd")
    print(res)
        