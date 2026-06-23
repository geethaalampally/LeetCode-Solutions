class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        reverse_alpha = "zyxwvutsrqponmlkjihgfedcba"

        for word in words:
            sumi = 0

            for char in word:
                sumi += weights[ord(char) - ord('a')]

            idx = sumi % 26
            res += reverse_alpha[idx]

        return res
                    






        