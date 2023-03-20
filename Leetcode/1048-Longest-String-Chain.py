from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dic = {}
        res = 0

        for word in words:
            cur = 1
            for i in range(len(word)):
                tmp = word[:i] + word[i+1:]
                if tmp in dic:
                    cur = max(cur, dic[tmp] + 1)
                dic[word] = cur
                res = max(res, dic[word])
        return res

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())