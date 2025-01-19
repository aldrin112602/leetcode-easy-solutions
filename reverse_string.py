def reverse_string(s: str) -> str:
    reversed_str = ""
    i = len(s)
    while i > 0:
        char = s[i - 1]
        reversed_str += char
        i -= 1
    return reversed_str