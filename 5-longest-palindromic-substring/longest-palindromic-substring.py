class Solution:
    def longestPalindrome(self, s: str) -> str:
        # If the string is empty or has one character, it's already a palindrome
        if len(s) < 2:
            return s  # Return the string itself
        
        start = 0  # Start index of the longest palindrome found
        end = 0    # End index of the longest palindrome found
        
        # Helper function to expand around the center
        def expandAroundCenter(left: int, right: int) -> None:
            nonlocal start, end  # Use the outer variables
            # Expand as long as the characters match and indices are valid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # Move left pointer to the left
                right += 1  # Move right pointer to the right
            # Update the longest palindrome if the current one is longer
            if right - left - 1 > end - start:
                start = left + 1  # Update start index
                end = right - 1   # Update end index
        
        # Try every possible center for odd and even length palindromes
        for i in range(len(s)):
            expandAroundCenter(i, i)      # Odd length palindrome
            expandAroundCenter(i, i + 1)  # Even length palindrome
        
        # Return the longest palindromic substring
        return s[start:end + 1]  # Return the substring from start to end (inclusive)