Str = "ABCDCBA"


def isPalindrome(s):
    left = 0
    right = len(s)-1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True

print(isPalindrome(Str))


def isPalindromeRec(s, left=0, right=None):
    if right is None:
        right = len(s) - 1

    # Move left pointer to next alphanumeric
    while left < right and not s[left].isalnum():
        left += 1

    # Move right pointer to previous alphanumeric
    while left < right and not s[right].isalnum():
        right -= 1

    # Base case: crossed pointers → all checks passed
    if left >= right:
        return True

    # If mismatch → not a palindrome
    if s[left].lower() != s[right].lower():
        return False

    # Recursive call inward
    return isPalindromeRec(s, left + 1, right - 1)
