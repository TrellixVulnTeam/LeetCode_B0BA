from typing import List


class Solution(object):
    def numMatchingSubseq(self, S, words):
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in S:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    print(sol.numMatchingSubseq(S, words))
