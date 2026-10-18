class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxl = 0
        seen = set()  # Stores the unique characters in the current window

        # Expand the window until we reach the end of the string
        while right < len(s):

            # If the current character is not already in the window
            if s[right] not in seen:
                seen.add(s[right])  # Add the character to the set

                # Update the maximum length of a substring without duplicates
                maxl = max(maxl, right - left + 1)

                # Move the right pointer to expand the window
                right += 1

            else:
                # A duplicate was found, so shrink the window from the left
                # until the duplicate character is removed from the set
                while s[right] in seen:
                    seen.remove(s[left])  # Remove the leftmost character
                    left += 1             # Move the left pointer forward

        # Return the length of the longest substring without repeating characters
        return maxl