def isAnagram(s: str, t: str) -> bool:
    counter = {}
    for letter in s:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    for letter in t:
        if letter not in counter:
            return False
        elif counter[letter] == 1:
            counter.pop(letter)
        elif counter[letter] > 1:
            counter[letter] -= 1

    return len(counter) == 0


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
