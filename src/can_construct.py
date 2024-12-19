def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    lookup = {}
    for i in range(len(magazine) - 1):
        if magazine[i] in lookup:
            lookup[magazine[i]] += 1
        else:
            lookup[magazine[i]] = 1

    for j in range(len(ransomNote) - 1):
        if ransomNote[j] in lookup and lookup[ransomNote[j]] > 0:
            lookup[ransomNote[j]] -= 1
            continue
        else:
            return False

    return True


ransomNote = "aab"
magazine = "aba"
print(canConstruct(ransomNote, magazine))
