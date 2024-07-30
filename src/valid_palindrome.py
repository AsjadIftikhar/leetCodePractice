def isPalindrome(s: str) -> bool:
    start, end = 0, len(s) - 1

    while start < end:
        while start < end and not (s[start].isalnum()):
            start += 1
        while start < end and not (s[end].isalnum()):
            end -= 1

        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True


# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = ".,"
print(isPalindrome(s))
