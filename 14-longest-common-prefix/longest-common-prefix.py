class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        i=0
        strs.sort()
        first=strs[0]
        last=strs[-1]

        while i<len(first) and i<len(last) and first[i]==last[i]:
            i+=1
        return first[:i]

#         if not strs:
#             return ""

#         sample = strs[0]

#         for i in range(len(sample)):

#             for j in range(1, len(strs)):

#                 if i >= len(strs[j]) or strs[j][i] != sample[i]:
#                     return sample[:i]

#         return sample