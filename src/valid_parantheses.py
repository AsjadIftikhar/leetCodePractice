def isValid(s: str) -> bool:
    stack = []
    for letter in s:
        if letter in ['(',  '[', '{']:
            stack.append(letter)
        if not stack:
            return False
        if letter == ')' and stack.pop() != '(':
            return False
        if letter == '}' and stack.pop() != '{':
            return False
        if letter == ']' and stack.pop() != '[':
            return False
    return stack == []

string = "]]]]"
print(isValid(string))