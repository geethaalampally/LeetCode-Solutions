class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # Stack stores indices
        # -1 acts as the boundary before the string starts
        stack = [-1]

        max_len = 0

        for i in range(len(s)):

            # Opening bracket -> store its index
            if s[i] == '(':
                stack.append(i)

            # Closing bracket
            else:
                # Match one opening bracket
                stack.pop()

                # No boundary left => invalid ')'
                if not stack:
                    # Current index becomes the new boundary
                    stack.append(i)

                else:
                    # Valid substring ends at i
                    curr_len = i - stack[-1]
                    max_len = max(max_len, curr_len)

        return max_len