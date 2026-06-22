class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0
        seen=set()
        left=0
        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
            seen.add(s[right])
            count=max(count,len(seen))
        return count