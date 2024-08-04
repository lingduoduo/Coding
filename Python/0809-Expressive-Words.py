from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def process(st):
            if not st:
                return [], []
            chars, counts = [st[0]], [1]
            for i in range(1, len(st)):
                if st[i] == chars[-1]:
                    counts[-1] += 1
                else:
                    chars.append(st[i])
                    counts.append(1)
            return chars, counts

        res = 0
        s_chars, s_counts = process(s)
        for word in words:
            w_chars, w_counts = process(word)

            if s_chars == w_chars:
                counter = 0
                for k in range(len(w_chars)):
                    if w_counts[k] == s_counts[k] or (
                        w_counts[k] < s_counts[k] and s_counts[k] >= 3
                    ):
                        counter += 1

                if counter == len(w_chars):
                    res += 1

        return res
