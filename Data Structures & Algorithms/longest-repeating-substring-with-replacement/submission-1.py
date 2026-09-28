class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}      # Stores the frequency of each character in the current window
        res = 0          # Stores the length of the longest valid window found

        l = 0            # Left pointer of the sliding window
        maxf = 0         # Highest frequency of any single character in the window

        for r in range(len(s)):
            # Add the current character to the window and update its frequency
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update the highest character frequency in the current window
            maxf = max(maxf, count[s[r]])

            # Number of characters that need to be replaced:
            # window length - frequency of the most common character
            #
            # If this is greater than k, the window is invalid,
            # so move the left pointer to shrink it.
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # Update the longest valid window length
            res = max(res, r - l + 1)

        return res