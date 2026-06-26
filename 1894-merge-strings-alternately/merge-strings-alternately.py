class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)

        res = []
        i = j = 0

        while i < n1 or j < n2:
            if i < n1:
                res.append(word1[i])
                i += 1

            if j < n2:
                res.append(word2[j])
                j += 1

        return "".join(res)