class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        sample = strs[0]

        for i in range(len(sample)):

            for j in range(1, len(strs)):

                if i >= len(strs[j]) or strs[j][i] != sample[i]:
                    return sample[:i]

        return sample